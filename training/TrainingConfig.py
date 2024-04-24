from dataclasses import dataclass


@dataclass
class TrainingConfig:
    image_size = 128  # the generated image resolution
    train_batch_size = 2  # Set to a higher number for training
    eval_batch_size = 16  # how many images to sample during evaluation (At least 16)
    num_epochs = 2  # Set to a higher number for training
    gradient_accumulation_steps = 1
    learning_rate = 1e-4
    lr_warmup_steps = 500
    save_image_epochs = 10
    save_model_epochs = 30
    mixed_precision = "fp16"  # `no` for float32, `fp16` for automatic mixed precision
    dataset_name = "./data/" # change it to the the local data ?"huggan/smithsonian_butterflies_subset"
    output_dir = (
        "models/ddpm-butterflies-128"  # the model name locally and on the HF Hub
    )
    push_to_hub = False  # whether to upload the saved model to the HF Hub
    # hub_model_id = "<your-username>/<my-awesome-model>"  # the name of the repository to create on the HF Hub
    hub_private_repo = False
    overwrite_output_dir = True  # overwrite the old model when re-running the notebook
    seed = 0
    number_of_noise_steps = 5  # Set to 1000 for training
