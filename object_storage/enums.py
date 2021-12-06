from enum import Enum


class FileStorages(Enum):

    covers = 'covers'

    @property
    def path(self):
        """По какому пути хранить файлы в Файловом хранилище."""
        if self is self.covers:
            return "covers/"


class FileMimetypes(Enum):
    # Картинки
    png = "image/png"
    jpeg = "image/jpeg"

    # Документы
    pdf = "application/pdf"

    # Архивы
    zip = "application/zip"
    rar = "application/x-rar-compressed"

    # Аудио-файлы
    wav = "audio/wav"
    mpeg = "audio/mpeg"
    mp3 = "audio/mp3"
    m4a = "audio/x-m4a"

    # Электронные книги
    epub = "application/epub+zip"

    # SQLFile
    sql = "application/sql"

    @property
    def file_format(self):
        if self is self.png:
            return ".png"
        elif self is self.jpeg:
            return ".jpg"
        elif self is self.pdf:
            return ".pdf"
        elif self is self.zip:
            return ".zip"
        elif self is self.wav:
            return ".wav"
        elif self is self.mpeg:
            return ".mpeg"
        elif self is self.mp3:
            return ".mp3"
        elif self is self.epub:
            return ".epub"
        elif self is self.m4a:
            return ".m4a"

    @classmethod
    def get_media_type_by_filename(cls, file_name: str) -> str:
        """
        Получаем медиа тип файла на основе его имени.

        :param file_name: "file.расширение."
        :return: Возвращается медиа тип, если расширение файла соответсвует названию одного из атрибутов класса
        None возвращается в случае, если расширение файл не соответствует ни одному названию атрибутов класса.
        """
        file_format = file_name.split('.')[-1]  # Получаем расширение файла. Название файла всегда "file.расширение"

        # В зависимости от расширения файла, определяем соответствующий медиа тип, указанный в атрибутах класса.
        if file_format == 'mp3':
            media_type = cls.mp3.value
        elif file_format == 'wav':
            media_type = cls.wav.value
        elif file_format == 'mpeg':
            media_type = cls.mpeg.value
        elif file_format == 'm4a':
            media_type = cls.m4a.value
        elif file_format == 'epub':
            media_type = cls.epub.value
        elif file_format == 'png':
            media_type = cls.png.value
        elif file_format in ['jpg', 'jpeg']:
            media_type = cls.jpeg.value
        elif file_format == 'zip':
            media_type = cls.zip.value
        else:
            media_type = None  # Не смогли найти соответствующий медиа тип атрибуту класса.

        return media_type  # Возвращаем медиа тип.

    @property
    def pillow_format(self):
        if self is self.png:
            return "PNG"
        elif self is self.jpeg:
            return "JPEG"


class UploadErrors(Enum):

    file_is_large = "Превышен лимит размера файла."
    mime_type_is_wrong_format = "Неподдерживаемый тип файла."
