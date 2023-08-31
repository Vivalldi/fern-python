
from fern.generator_exec.resources.config import GeneratorConfig
from fern.generator_exec.resources.readme import GenerateReadmeRequest, BadgeType
from fern_python.generator_exec_wrapper import GeneratorExecWrapper
from fern_python.codegen import Project
from .client_generator.root_client_generator import GeneratedRootClient


class CloudReadmeGenerator:

    def __init__(self, *, generator_config: GeneratorConfig, generator_exec_wrapper: GeneratorExecWrapper, project: Project, generated_root_client: GeneratedRootClient): 
        self._generator_config = generator_config
        self._generator_exec_wrapper = generator_exec_wrapper
        self._project = project
        self._generated_root_client = generated_root_client
    
    def generate_cloud_readme(self) -> bool: 
        output_mode = self._generator_config.output.mode.get_as_union()
        if output_mode.type == "github":
            publish_info = output_mode.publish_info.get_as_union()
            capitalized_org_name = self._generator_config.organization.capitalize()
            installation = None
            if publish_info.type == "pypi": 
                installation = self._get_installation(publish_info.package_name) 
            generate_readme_request = GenerateReadmeRequest(
                title=f"{capitalized_org_name} Python Library",
                badge=BadgeType.PYPI,
                summary=f"The {capitalized_org_name} Python Library provides convenient access to the {capitalized_org_name} API from applications written in Python.",
                installation=installation,
                usage=self._generated_root_client.usage,
                async_usage=self._generated_root_client.async_usage,
                requirements=["Python 3.7 or higher."],
            )
            return self._generator_exec_wrapper.generate_readme(generate_readme_request=generate_readme_request)
        else: 
            return False

    def _get_installation(self, package_name: str) -> str: 
        return f"""
```bash        
pip install {package_name}
# or
poetry add {package_name}
```
"""
