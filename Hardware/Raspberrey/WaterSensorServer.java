import com.pi4j.io.gpio.*;
import com.pi4j.io.gpio.event.GpioPinDigitalStateChangeEvent;
import com.pi4j.io.gpio.event.GpioPinListenerDigital;
import java.io.*;
import java.net.*;

public class WaterSensorServer {
    private static final int WATER_SENSOR_PIN = RaspiPin.GPIO_04; // GPIO pin connected to the water sensor
    private static final int SAMPLE_INTERVAL = 1000; // Sampling interval in milliseconds

    public static void main(String[] args) {
        try {
            // Initialize the GPIO controller
            GpioController gpio = GpioFactory.getInstance();

            // Initialize the water sensor pin
            GpioPinDigitalInput waterSensor = gpio.provisionDigitalInputPin(WATER_SENSOR_PIN, PinPullResistance.PULL_DOWN);

            // Initialize the server socket
            int port = 12345;
            ServerSocket serverSocket = new ServerSocket(port);
            System.out.println("Water Sensor Server is running on port " + port);

            // Add a listener to monitor water sensor changes
            waterSensor.addListener(new GpioPinListenerDigital() {
                @Override
                public void handleGpioPinDigitalStateChangeEvent(GpioPinDigitalStateChangeEvent event) {
                    boolean isWet = event.getState() == PinState.HIGH;
                    if (isWet) {
                        System.out.println("Plant is wet");
                    } else {
                        System.out.println("Plant is dry");
                    }
                }
            });

            while (true) {
                Socket clientSocket = serverSocket.accept();
                PrintWriter out = new PrintWriter(clientSocket.getOutputStream(), true);

                // Simulate getting water level from the sensor
                boolean isWet = waterSensor.isHigh();

                // Send the water level percentage to the client
                int waterLevel = isWet ? 100 : 0;
                out.println("Water level: " + waterLevel + "%");

                clientSocket.close();

                // Delay before the next sensor reading
                Thread.sleep(SAMPLE_INTERVAL);
            }
        } catch (IOException | InterruptedException e) {
            e.printStackTrace();
        }
    }
}
