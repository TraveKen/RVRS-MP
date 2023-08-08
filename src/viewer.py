import math

from PIL import Image
from textual import events
from textual.app import RenderResult
from textual.widget import Widget

from textual_imageview.img import ImageView


class ImageViewer(Widget):
    DEFAULT_CSS = """
    ImageViewer{
        min-width: 8;
        min-height: 8;
    }
    """

    def __init__(self, image: Image.Image):
        super().__init__()
        if not isinstance(image, Image.Image):
            raise TypeError(
                f"Expected PIL Image, but received '{type(image).__name__}' instead."
            )

        self.image = ImageView(image)
        self.mouse_down = False

    def on_show(self):
        self.old_width = self.size.width
        self.old_height = self.size.height
        w, h = self.size.width, self.size.height
        img_w, img_h = self.image.size

        # Compute zoom such that image fits in container
        zoom_w = math.log(max(w, 1) / img_w, self.image.ZOOM_RATE)
        zoom_h = math.log((max(h, 1) * 2) / img_h, self.image.ZOOM_RATE)
        zoom = max(0, math.ceil(max(zoom_w, zoom_h)))
        self.image.set_zoom(zoom)

        # Position image in center of container
        img_w, img_h = self.image.zoomed_size
        self.image.origin_position = (-round((w - img_w) / 2), -round(h - img_h / 2))
        self.image.set_container_size(w, h, maintain_center=False)

        self.refresh()


    def on_resize(self, event: events.Resize):
        self.image.set_container_size(event.size.width, event.size.height)
        self.on_show()
        self.refresh()
        #event.stop()

    def render(self) -> RenderResult:
        return self.image



    def update(self, image: Image.Image):
        self.image = ImageView(image)
        try:
            self.image.set_container_size(self.old_width,self.old_height)
            self.on_show()
        except AttributeError:
            pass
        self.refresh()
