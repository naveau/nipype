# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from ....testing import assert_equal
from ..legacy import GenWarpFields

def test_GenWarpFields_inputs():
    input_map = dict(args=dict(argstr='%s',
    ),
    bias_field_correction=dict(argstr='-n 1',
    ),
    dimension=dict(argstr='-d %d',
    position=1,
    usedefault=True,
    ),
    environ=dict(nohash=True,
    usedefault=True,
    ),
    force_proceed=dict(argstr='-f 1',
    ),
    ignore_exception=dict(nohash=True,
    usedefault=True,
    ),
    input_image=dict(argstr='-i %s',
    copyfile=False,
    mandatory=True,
    ),
    inverse_warp_template_labels=dict(argstr='-l',
    ),
    max_iterations=dict(argstr='-m %s',
    sep='x',
    ),
    num_threads=dict(nohash=True,
    usedefault=True,
    ),
    out_prefix=dict(argstr='-o %s',
    usedefault=True,
    ),
    quality_check=dict(argstr='-q 1',
    ),
    reference_image=dict(argstr='-r %s',
    copyfile=True,
    mandatory=True,
    ),
    similarity_metric=dict(argstr='-s %s',
    ),
    terminal_output=dict(nohash=True,
    ),
    transformation_model=dict(argstr='-t %s',
    usedefault=True,
    ),
    )
    inputs = GenWarpFields.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            yield assert_equal, getattr(inputs.traits()[key], metakey), value

def test_GenWarpFields_outputs():
    output_map = dict(affine_transformation=dict(),
    input_file=dict(),
    inverse_warp_field=dict(),
    output_file=dict(),
    warp_field=dict(),
    )
    outputs = GenWarpFields.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            yield assert_equal, getattr(outputs.traits()[key], metakey), value

