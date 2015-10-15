# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from .....testing import assert_equal
from ..gtract import gtractConcatDwi

def test_gtractConcatDwi_inputs():
    input_map = dict(args=dict(argstr='%s',
    ),
    environ=dict(nohash=True,
    usedefault=True,
    ),
    ignoreOrigins=dict(argstr='--ignoreOrigins ',
    ),
    ignore_exception=dict(nohash=True,
    usedefault=True,
    ),
    inputVolume=dict(argstr='--inputVolume %s...',
    ),
    numberOfThreads=dict(argstr='--numberOfThreads %d',
    ),
    outputVolume=dict(argstr='--outputVolume %s',
    hash_files=False,
    ),
    terminal_output=dict(nohash=True,
    ),
    )
    inputs = gtractConcatDwi.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            yield assert_equal, getattr(inputs.traits()[key], metakey), value

def test_gtractConcatDwi_outputs():
    output_map = dict(outputVolume=dict(),
    )
    outputs = gtractConcatDwi.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            yield assert_equal, getattr(outputs.traits()[key], metakey), value

