import javax.swing.text.html.ImageView;
import java.awt.*;
import java.awt.image.ImageObserver;
import java.awt.image.ImageProducer;

public class LoginUI extends Application{
    //A button with an empty text caption.
    Button button1 = new Button();
    //A button with the specified text caption.
    Button button2 = new Button("Accept");
    //A button with the specified text caption and icon.
    Image imageOk = new Image(getClass().getResourceAsStream("ok.png")) {
        @Override
        public int getWidth(ImageObserver imageObserver) {
            return 0;
        }

        @Override
        public int getHeight(ImageObserver imageObserver) {
            return 0;
        }

        @Override
        public ImageProducer getSource() {
            return null;
        }

        @Override
        public Graphics getGraphics() {
            return null;
        }

        @Override
        public Object getProperty(String s, ImageObserver imageObserver) {
            return null;
        }
    };

    public LoginUI() {
        button3 = new Button("Accept", new ImageView(imageOk));
    }
}
