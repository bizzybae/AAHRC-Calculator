#!/usr/bin/env python3
"""
AAHRC Project - NHANES Data Downloader
Automatically downloads NHANES 2017-2020 cycle data for:
- Albuminuria (urine albumin-creatinine ratio)
- Blood pressure
- Demographics
- Additional cardiovascular risk factors
"""

import os
import requests
import pyreadstat
import pandas as pd
from pathlib import Path
import logging

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Define data paths
BASE_DIR = Path(__file__).resolve().parent.parent.parent
DATA_RAW = BASE_DIR / 'data' / 'raw'
DATA_RAW.mkdir(parents=True, exist_ok=True)

# NHANES 2017-2020 Dataset URLs
NHANES_DATASETS = {
    '2017-2018': {
        'albuminuria': 'https://wwwn.cdc.gov/Nchs/Nhanes/2017-2018/ALB_CR_J.XPT',
        'blood_pressure': 'https://wwwn.cdc.gov/Nchs/Nhanes/2017-2018/BPX_J.XPT',
        'demographics': 'https://wwwn.cdc.gov/Nchs/Nhanes/2017-2018/DEMO_J.XPT',
        'body_measures': 'https://wwwn.cdc.gov/Nchs/Nhanes/2017-2018/BMX_J.XPT',
        'cholesterol': 'https://wwwn.cdc.gov/Nchs/Nhanes/2017-2018/TCHOL_J.XPT',
        'diabetes': 'https://wwwn.cdc.gov/Nchs/Nhanes/2017-2018/GHB_J.XPT',
    }
}

def download_file(url, destination):
    """
    Download a file from URL to destination path.
    
    Args:
        url (str): URL to download from
        destination (Path): Local file path to save to
    
    Returns:
        bool: True if successful, False otherwise
    """
    try:
        logger.info(f"Downloading {url}")
        response = requests.get(url, stream=True, timeout=60)
        response.raise_for_status()
        
        with open(destination, 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)
        
        logger.info(f"Successfully downloaded to {destination}")
        return True
    except Exception as e:
        logger.error(f"Failed to download {url}: {str(e)}")
        return False

def convert_xpt_to_csv(xpt_file, csv_file):
    """
    Convert SAS .XPT file to CSV format.
    
    Args:
        xpt_file (Path): Path to .XPT file
        csv_file (Path): Path to output CSV file
    
    Returns:
        pd.DataFrame: The converted data
    """
    try:
        logger.info(f"Converting {xpt_file.name} to CSV")
        df, meta = pyreadstat.read_xport(str(xpt_file))
        df.to_csv(csv_file, index=False)
        logger.info(f"Converted to {csv_file.name}. Shape: {df.shape}")
        return df
    except Exception as e:
        logger.error(f"Failed to convert {xpt_file}: {str(e)}")
        return None

def download_nhanes_cycle(cycle, datasets):
    """
    Download all datasets for a specific NHANES cycle.
    
    Args:
        cycle (str): Cycle identifier (e.g., '2017-2018')
        datasets (dict): Dictionary of dataset names and URLs
    
    Returns:
        dict: Dictionary of dataframes for each dataset
    """
    cycle_dir = DATA_RAW / cycle.replace('-', '_')
    cycle_dir.mkdir(parents=True, exist_ok=True)
    
    dataframes = {}
    
    for dataset_name, url in datasets.items():
        filename = url.split('/')[-1]
        xpt_path = cycle_dir / filename
        csv_path = cycle_dir / filename.replace('.XPT', '.csv')
        
        # Download if not already present
        if not xpt_path.exists():
            success = download_file(url, xpt_path)
            if not success:
                continue
        else:
            logger.info(f"{filename} already exists, skipping download")
        
        # Convert to CSV if not already done
        if not csv_path.exists():
            df = convert_xpt_to_csv(xpt_path, csv_path)
            if df is not None:
                dataframes[dataset_name] = df
        else:
            logger.info(f"{csv_path.name} already exists")
            try:
                dataframes[dataset_name] = pd.read_csv(csv_path)
            except Exception as e:
                logger.error(f"Failed to read {csv_path}: {str(e)}")
    
    return dataframes

def main():
    """
    Main execution function.
    """
    logger.info("=" * 60)
    logger.info("AAHRC Project - NHANES Data Download Starting")
    logger.info("=" * 60)
    
    all_data = {}
    
    for cycle, datasets in NHANES_DATASETS.items():
        logger.info(f"\nProcessing NHANES cycle: {cycle}")
        cycle_data = download_nhanes_cycle(cycle, datasets)
        all_data[cycle] = cycle_data
    
    logger.info("\n" + "=" * 60)
    logger.info("Download Summary:")
    for cycle, data in all_data.items():
        logger.info(f"  {cycle}: {len(data)} datasets successfully loaded")
        for name, df in data.items():
            logger.info(f"    - {name}: {df.shape[0]} rows, {df.shape[1]} columns")
    
    logger.info("=" * 60)
    logger.info("NHANES Data Download Complete!")
    logger.info(f"Data saved to: {DATA_RAW}")
    logger.info("=" * 60)

if __name__ == "__main__":
    main()
