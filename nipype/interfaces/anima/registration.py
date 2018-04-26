from nipype.interfaces.base import (
    CommandLine,
    CommandLineInputSpec,
    TraitedSpec,
    File,
    traits
)
import os




class PyramidalBMRegistrationInputSpec(CommandLineInputSpec):

    moving_image = File(exists=True, argstr='-m %s', mandatory=True,
                   desc='Moving image')
    fixed_image = File(exists=True, argstr='-r %s', mandatory=True,
                   desc='Fixed image')
    output_image = File(argstr='-o %s', mandatory=True,
                    desc='Output (registered) image')
    output_transform = File(argstr='-O %s',
                    desc='Output transformation')

class PyramidalBMRegistrationOutputSpec(TraitedSpec):
     output_image = File(desc = 'Output (registered) image', exists = True)
     output_transform = File(desc = 'Output transformation', exists = True)

class PyramidalBMRegistration(CommandLine):

    _cmd = 'animaPyramidalBMRegistration'

    input_spec = PyramidalBMRegistrationInputSpec
    output_spec = PyramidalBMRegistrationOutputSpec

    def _list_outputs(self):
        outputs = self.output_spec().get()
        outputs['output_image'] = os.path.abspath(self.inputs.output_image)
        outputs['output_transform'] = os.path.abspath(self.inputs.output_transform)
        return outputs
