from faster_whisper import WhisperModel

model_size = "large_v3"

model = WhisperModel(model_size, device='cpu', compute_type='float16')
