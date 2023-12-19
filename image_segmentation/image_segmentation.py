import tensorflow
import tensorflow_datasets as datasets

builder = datasets.builder("oxford_iiit_pet")

config = datasets.download.DownloadConfig(register_cehcksums = True)

builder.download_and_prepare(download_config = config)

dataset = builder.as_dataset()