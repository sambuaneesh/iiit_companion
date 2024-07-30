# Usage Guide

This guide will walk you through how to use the IIIT Companion application, including creating custom dashboards and interacting with the generated apps.

## Launching the Application

1. Open a terminal or command prompt.
2. Navigate to the project root directory.
3. Run the following command:
   ```
   python run.py
   ```
4. Open a web browser and go to `http://localhost:8501` (or the port specified in your configuration).

## Using the IIIT Companion Builder

1. On the main page, you'll see the IIIT Companion Builder interface.
2. The interface is divided into several sections, each representing a category of features:
   - Environmental
   - Resource
   - Academic
   - Event
   - Health

3. For each category, select the features you want to include in your personalized dashboard by clicking the checkboxes.

4. After selecting your desired features, click the "Create My IIIT Companion App" button at the bottom of the page.

5. If successful, you'll see a success message with a URL to access your personalized dashboard.

## Interacting with Your Personalized Dashboard

1. Click on the provided URL or copy and paste it into a new browser tab.

2. Your personalized dashboard will load, displaying the features you selected:

   - **Environmental Data**: View real-time temperature, humidity, and air quality information.
   - **Resource Availability**: Check library occupancy, cafeteria menu, or study room availability.
   - **Academic Information**: See upcoming assignments, class schedules, or recent grades.
   - **Campus Events**: Stay updated on upcoming events, club activities, or workshops.
   - **Health & Wellness**: Receive wellness tips, fitness suggestions, or mental health resources.

3. The dashboard will automatically refresh its data periodically to provide up-to-date information.

## Creating Multiple Dashboards

You can create multiple personalized dashboards by returning to the IIIT Companion Builder page and selecting different combinations of features. Each generated dashboard will have its own unique URL.

## Sharing Your Dashboard

You can share your personalized dashboard with others by sending them the URL. Note that in the current implementation, all generated dashboards are publicly accessible to anyone with the URL.

## Refreshing Data

Most data on your dashboard will update automatically. However, if you want to manually refresh the data:

1. Look for a "Refresh" button on your dashboard (if implemented).
2. Alternatively, you can refresh your browser page to fetch the latest data.

## Closing the Application

To stop the IIIT Companion application:

1. Return to the terminal where you ran the `python run.py` command.
2. Press `Ctrl+C` to stop the application.
3. This will shut down both the main Streamlit app and all the microservices.

## Next Steps

- To learn how to customize and extend the IIIT Companion app, see the [Customization Guide](CUSTOMIZATION.md).
- For information on how the app works behind the scenes, check out the [Architecture Overview](ARCHITECTURE.md).
- If you encounter any issues, refer to the [Troubleshooting](TROUBLESHOOTING.md) guide.
