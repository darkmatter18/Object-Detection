class BaseDetection:
    def save(self, video: bytes, content_type: str) -> str:
        import tempfile
        import mimetypes
        
        ext = mimetypes.guess_extension(content_type)
        if ext is None:
            raise ValueError(f"Unknown content type: {content_type}")
        
        with tempfile.NamedTemporaryFile(delete=False, suffix=ext) as f:
            f.write(video)
            return f.name
