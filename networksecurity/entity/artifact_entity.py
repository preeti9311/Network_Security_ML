from dataclasses import dataclass


@dataclass
class ArtifactEntity:
    training_data_file_path: str
    testing_data_file_path: str