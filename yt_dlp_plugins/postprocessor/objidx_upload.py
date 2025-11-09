"""yt-dlp postprocessor plugin to upload files to OI"""

from yt_dlp.postprocessor.common import PostProcessor, PostProcessingError
from obj_idx import client as oic
from obj_idx import dlp_lpm_meta as oih

# TODO postprocessor hook for upload progress

class ObjIdxUploadPP(PostProcessor):
    """OI uploader postprocessor"""
    def __init__(self, downloader=None, oibucket=None, oipartial=False, lpmlib=None, **kwargs):
        # NOTE Also, "downloader", "when" and "key" are reserved names
        super().__init__(downloader)
        self._kwargs = kwargs
        self.oibucket = oibucket
        # NOTE we don't actually throw an error until run.
        if not oibucket:
            self.to_screen('No OI bucket; cannot upload.')
        try:
            self.objidx_client = oic.get_obj_idx_env()
        except KeyError as e:
            self.objidx_client = None
            self.to_screen(f'Cannot connect to OI because {str(e)}')
        self.oipartial = oipartial
        self.lpmlib = lpmlib


    def run(self, information):
        """Run the upload"""
        if not (self.objidx_client and self.oibucket):
            raise PostProcessingError('Not uploading because missing OI info')
        metadata = oih.DLPMetaData(information, partial=self.oipartial)
        if self.lpmlib:
            metadata.add_lpm(self.lpmlib)
        self.to_screen('Attempting OI upload...')
        try:
            oif = metadata.upload(self.objidx_client, self.oibucket)
        except Exception as e:
            raise PostProcessingError(str(e)) from e
        self.to_screen(f'Uploaded as {oif.uuid}')
        information['oi_uuid'] = oif.uuid
        assert oif.object['completed']
        assert not oif.object['deleted']
        return [str(metadata.get_media_file())], information
