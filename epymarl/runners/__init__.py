REGISTRY = {}

from . import episode_runner

REGISTRY["episode"] = episode_runner.EpisodeRunner

from . import parallel_runner
REGISTRY["parallel"] = parallel_runner.ParallelRunner

from . import nstep_runner
REGISTRY["nstep"] = nstep_runner.NStepRunner
