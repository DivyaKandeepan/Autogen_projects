from typing import Dict, Union
from IPython import get_ipython
import autogen
class IPythonUserProxyAgent(autogen.UserProxyAgent):
    def generate_init_message(self, *args, **kwargs) -> Union[str, Dict]:
    return super().generate_init_message(*args, **kwargs) + """If you suggest code, the code will be executed in IPython."""
def run_code(self, code, **kwargs):
    result = self._ipython.run_cell("%%capture --no-display cap\n" + code)
    log = self._ipython.ev("cap.stdout")
    log += self._ipython.ev("cap.stderr")
    if result.result is not None:
        log += str(result.result)
    exitcode = 0 if result.success else 1
    if result.error_before_exec is not None:
        log += f"\n{result.error_before_exec}"
        exitcode = 1
    if result.error_in_exec is not None:
        log += f"\n{result.error_in_exec}"
        exitcode = 1
    return exitcode, log, None