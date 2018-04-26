from nipype.interfaces.anima import PyramidalBMRegistration
from nipype.interfaces.base import (
    File
)
import os


def test_PyramidalBMRegistrationI():
    i = PyramidalBMRegistration()
    assert i.cmd == 'animaPyramidalBMRegistration'

    i.inputs.moving_image = 'nipype/testing/data/tpm_00.nii.gz'
    i.inputs.fixed_image = 'nipype/testing/data/tpm_00.nii.gz'
    i.inputs.output_image = 'nipype/testing/data/tpm_00_warped.nii.gz'
    i.inputs.output_transform = 'nipype/testing/data/tpm_00_warped.txt'

    results = i.run()

    assert os.path.abspath(results.outputs.output_image) == os.path.abspath(i.inputs.output_image)
    os.remove(os.path.abspath(results.outputs.output_image))
    assert os.path.abspath(results.outputs.output_transform) == os.path.abspath(i.inputs.output_transform)
    os.remove(os.path.abspath(results.outputs.output_transform))
