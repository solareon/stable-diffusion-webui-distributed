import logging
from rich.logging import RichHandler
from modules.shared import cmd_opts

log_level = 'DEBUG' if cmd_opts.distributed_debug else 'INFO'
logger = logging.getLogger("rich")
logger.addHandler(RichHandler(rich_tracebacks=True, markup=True))
logger.setLevel(log_level)

warmup_samples = 2  # number of samples to do before recording a valid benchmark sample
benchmark_payload: dict = {
    "prompt": "A herd of cows grazing at the bottom of a sunny valley",
    "negative_prompt": "",
    "steps": 20,
    "width": 512,
    "height": 512,
    "batch_size": 1
}
