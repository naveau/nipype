# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from __future__ import unicode_literals
from ..preprocess import MRIConvert


def test_MRIConvert_inputs():
    input_map = dict(
        apply_inv_transform=dict(argstr='--apply_inverse_transform %s', ),
        apply_transform=dict(argstr='--apply_transform %s', ),
        args=dict(argstr='%s', ),
        ascii=dict(argstr='--ascii', ),
        autoalign_matrix=dict(argstr='--autoalign %s', ),
        color_file=dict(argstr='--color_file %s', ),
        conform=dict(argstr='--conform', ),
        conform_min=dict(argstr='--conform_min', ),
        conform_size=dict(argstr='--conform_size %s', ),
        crop_center=dict(argstr='--crop %d %d %d', ),
        crop_gdf=dict(argstr='--crop_gdf', ),
        crop_size=dict(argstr='--cropsize %d %d %d', ),
        cut_ends=dict(argstr='--cutends %d', ),
        cw256=dict(argstr='--cw256', ),
        devolve_transform=dict(argstr='--devolvexfm %s', ),
        drop_n=dict(argstr='--ndrop %d', ),
        environ=dict(
            nohash=True,
            usedefault=True,
        ),
        fill_parcellation=dict(argstr='--fill_parcellation', ),
        force_ras=dict(argstr='--force_ras_good', ),
        frame=dict(argstr='--frame %d', ),
        frame_subsample=dict(argstr='--fsubsample %d %d %d', ),
        fwhm=dict(argstr='--fwhm %f', ),
        ignore_exception=dict(
            deprecated='1.0.0',
            nohash=True,
            usedefault=True,
        ),
        in_center=dict(argstr='--in_center %s', ),
        in_file=dict(
            argstr='--input_volume %s',
            mandatory=True,
            position=-2,
        ),
        in_i_dir=dict(argstr='--in_i_direction %f %f %f', ),
        in_i_size=dict(argstr='--in_i_size %d', ),
        in_info=dict(argstr='--in_info', ),
        in_j_dir=dict(argstr='--in_j_direction %f %f %f', ),
        in_j_size=dict(argstr='--in_j_size %d', ),
        in_k_dir=dict(argstr='--in_k_direction %f %f %f', ),
        in_k_size=dict(argstr='--in_k_size %d', ),
        in_like=dict(argstr='--in_like %s', ),
        in_matrix=dict(argstr='--in_matrix', ),
        in_orientation=dict(argstr='--in_orientation %s', ),
        in_scale=dict(argstr='--scale %f', ),
        in_stats=dict(argstr='--in_stats', ),
        in_type=dict(argstr='--in_type %s', ),
        invert_contrast=dict(argstr='--invert_contrast %f', ),
        midframe=dict(argstr='--mid-frame', ),
        no_change=dict(argstr='--nochange', ),
        no_scale=dict(argstr='--no_scale 1', ),
        no_translate=dict(argstr='--no_translate', ),
        no_write=dict(argstr='--no_write', ),
        out_center=dict(argstr='--out_center %f %f %f', ),
        out_datatype=dict(argstr='--out_data_type %s', ),
        out_file=dict(
            argstr='--output_volume %s',
            genfile=True,
            position=-1,
        ),
        out_i_count=dict(argstr='--out_i_count %d', ),
        out_i_dir=dict(argstr='--out_i_direction %f %f %f', ),
        out_i_size=dict(argstr='--out_i_size %d', ),
        out_info=dict(argstr='--out_info', ),
        out_j_count=dict(argstr='--out_j_count %d', ),
        out_j_dir=dict(argstr='--out_j_direction %f %f %f', ),
        out_j_size=dict(argstr='--out_j_size %d', ),
        out_k_count=dict(argstr='--out_k_count %d', ),
        out_k_dir=dict(argstr='--out_k_direction %f %f %f', ),
        out_k_size=dict(argstr='--out_k_size %d', ),
        out_matrix=dict(argstr='--out_matrix', ),
        out_orientation=dict(argstr='--out_orientation %s', ),
        out_scale=dict(argstr='--out-scale %d', ),
        out_stats=dict(argstr='--out_stats', ),
        out_type=dict(argstr='--out_type %s', ),
        parse_only=dict(argstr='--parse_only', ),
        read_only=dict(argstr='--read_only', ),
        reorder=dict(argstr='--reorder %d %d %d', ),
        resample_type=dict(argstr='--resample_type %s', ),
        reslice_like=dict(argstr='--reslice_like %s', ),
        sdcm_list=dict(argstr='--sdcmlist %s', ),
        skip_n=dict(argstr='--nskip %d', ),
        slice_bias=dict(argstr='--slice-bias %f', ),
        slice_crop=dict(argstr='--slice-crop %d %d', ),
        slice_reverse=dict(argstr='--slice-reverse', ),
        smooth_parcellation=dict(argstr='--smooth_parcellation', ),
        sphinx=dict(argstr='--sphinx', ),
        split=dict(argstr='--split', ),
        status_file=dict(argstr='--status %s', ),
        subject_name=dict(argstr='--subject_name %s', ),
        subjects_dir=dict(),
        te=dict(argstr='-te %d', ),
        template_info=dict(),
        template_type=dict(argstr='--template_type %s', ),
        terminal_output=dict(
            deprecated='1.0.0',
            nohash=True,
        ),
        ti=dict(argstr='-ti %d', ),
        tr=dict(argstr='-tr %d', ),
        unwarp_gradient=dict(argstr='--unwarp_gradient_nonlinearity', ),
        vox_size=dict(argstr='-voxsize %f %f %f', ),
        zero_ge_z_offset=dict(argstr='--zero_ge_z_offset', ),
        zero_outlines=dict(argstr='--zero_outlines', ),
    )
    inputs = MRIConvert.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value
def test_MRIConvert_outputs():
    output_map = dict(out_file=dict(), )
    outputs = MRIConvert.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value
