This repository contains a plugin package for [yt-dlp](https://github.com/yt-dlp/yt-dlp#readme) which is a post-processor that uploads to [Object Index](https://github.com/ctengel/objectindex) when a download is complete. 


## Installation

Requires yt-dlp `2023.01.02` or above, and requires object-index `0.2.4` or above.

You can install this package with pip:
```
python3 -m pip install -U https://github.com/ctengel/yt-dlp-obj-idx/archive/master.zip
```

See [installing yt-dlp plugins](https://github.com/yt-dlp/yt-dlp#installing-plugins) for the other methods this plugin package can be installed.


## Usage

When running yt-dlp this can be added as a postprocessor, like so.

`yt-dlp --use-postprocessor ObjIdxUploadPP:oibucket=mybucket`

Possible options (semicolon separated):
- oibucket (mandatory) - name of object index bucket to upload to
- oipartial (optional) - set to true or anything nonempty to specify that these uploads should be considered partial representations of their respective URLs
- lpmlib (optional) - LPM libary (experimental)
- when - set a different time to run it (see yt-dlp docs)

It is required to set the usual `OBJIDX_URL` and `OBJIDX_AUTH` environment variables as well.

## Development

See the [Plugin Development](https://github.com/yt-dlp/yt-dlp/wiki/Plugin-Development) section of the yt-dlp wiki.
