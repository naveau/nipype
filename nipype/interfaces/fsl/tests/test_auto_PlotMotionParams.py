# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from ....testing import assert_equal
from ..utils import PlotMotionParams

def test_PlotMotionParams_inputs():
    input_map = dict(args=dict(argstr='%s',
    ),
    environ=dict(nohash=True,
    usedefault=True,
    ),
    ignore_exception=dict(nohash=True,
    usedefault=True,
    ),
    in_file=dict(argstr='%s',
    mandatory=True,
    position=1,
    ),
    in_source=dict(mandatory=True,
    ),
    out_file=dict(argstr='-o %s',
    genfile=True,
    hash_files=False,
    ),
    output_type=dict(),
    plot_size=dict(argstr='%s',
    ),
    plot_type=dict(argstr='%s',
    mandatory=True,
    ),
    terminal_output=dict(nohash=True,
    ),
    )
    inputs = PlotMotionParams.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            yield assert_equal, getattr(inputs.traits()[key], metakey), value

def test_PlotMotionParams_outputs():
    output_map = dict(out_file=dict(),
    )
    outputs = PlotMotionParams.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            yield assert_equal, getattr(outputs.traits()[key], metakey), value

