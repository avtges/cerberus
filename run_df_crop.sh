python rm_ds_store.py

python auto_fake_vid_split.py deepfake_videos generate
python auto_deepfake_crop.py generate deepfake_facecrops
python create_deepfake_csv.py deepfake_facecrops deepfake
