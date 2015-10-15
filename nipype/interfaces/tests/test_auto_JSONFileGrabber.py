# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from ...testing import assert_equal
from ..io import JSONFileGrabber

def test_JSONFileGrabber_inputs():
    input_map = dict(defaults=dict(),
    ignore_exception=dict(nohash=True,
    usedefault=True,
    ),
    in_file=dict(),
    )
    inputs = JSONFileGrabber.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            yield assert_equal, getattr(inputs.traits()[key], metakey), value

def test_JSONFileGrabber_outputs():
    output_map = dict()
    outputs = JSONFileGrabber.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            yield assert_equal, getattr(outputs.traits()[key], metakey), value

