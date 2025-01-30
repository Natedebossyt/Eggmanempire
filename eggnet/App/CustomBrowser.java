import javafx.application.Application;
import javafx.scene.Scene;
import javafx.scene.control.Button;
import javafx.scene.control.TextField;
import javafx.scene.layout.BorderPane;
import javafx.scene.web.WebView;
import javafx.stage.Stage;

public class CustomBrowser extends Application {

    @Override
    public void start(Stage primaryStage) {
        // Create a WebView (browser rendering component)
        WebView webView = new WebView();
        webView.getEngine().load("http://www.example.com");  // Load default URL

        // Create a simple text field for URL input
        TextField urlField = new TextField("http://www.example.com");

        // Create a button to load the URL from the text field
        Button goButton = new Button("Go");
        goButton.setOnAction(e -> webView.getEngine().load(urlField.getText()));

        // Layout: Place the URL field at the top and WebView in the center
        BorderPane root = new BorderPane();
        root.setTop(urlField);
        root.setCenter(webView);
        root.setBottom(goButton);

        // Create and set the scene
        Scene scene = new Scene(root, 800, 600);
        primaryStage.setTitle("Custom Java Browser");
        primaryStage.setScene(scene);
        primaryStage.show();
    }

    public static void main(String[] args) {
        launch(args);  // Start the JavaFX application
    }
}