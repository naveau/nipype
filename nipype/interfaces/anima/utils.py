from nipype.interfaces.base import (
	CommandLine,
	CommandLineInputSpec,
    TraitedSpec,
	File,
    traits
)
import os

class CropImageInputSpec(CommandLineInputSpec):
    def get_desc_size(dimension):
        return (
        'Size of ROI for the {}index dimension. '
        'The resulting croped image will go from {}index to {}size along the {}index axis. '
        'If 0 the dimension is collapsed.').format(
            dimension, dimension, dimension, dimension
        )

    def get_desc_index(dimension):
        return (
        'Start of ROI for the {}index dimension. '
        'The resulting croped image will go from {}index to {}size along the {}index axis.').format(
            dimension, dimension, dimension, dimension
        )

    in_file = File(exists=True, argstr='-i %s', mandatory=True,
                   desc='Input image to crop')
    out_file = File(argstr='-o %s', mandatory=True,
	                desc='Output cropped image')
    tsize = traits.Int(argstr='-T %d', desc=get_desc_size('t'))
    tindex = traits.Int(argstr='-t %d', desc=get_desc_index('t'))
    zsize = traits.Int(argstr='-Z %d', desc=get_desc_size('z'))
    zindex = traits.Int(argstr='-z %d', desc=get_desc_index('z'))
    ysize = traits.Int(argstr='-Y %d', desc=get_desc_size('y'))
    yindex = traits.Int(argstr='-y %d', desc=get_desc_index('y'))
    xsize = traits.Int(argstr='-X %d', desc=get_desc_size('x'))
    xindex = traits.Int(argstr='-x %d', desc=get_desc_index('x'))
    bounding_box = traits.File(
        exists=True,
        argstr='-m %s',
        desc='A mask used instead of other arguments to determine a bounding box',
        xor=['tsize', 'tindex', 'zsize', 'zindex', 'ysize', 'yindex', 'xsize', 'xindex']
    )

class CropImageOutputSpec(TraitedSpec):
     out_file = File(desc = "Cropped Image", exists = True)

class CropImage(CommandLine):

    _cmd = 'animaCropImage'

    input_spec = CropImageInputSpec
    output_spec = CropImageOutputSpec

    def _list_outputs(self):
        outputs = self.output_spec().get()
        outputs['out_file'] = os.path.abspath(self.inputs.out_file)
        return outputs
