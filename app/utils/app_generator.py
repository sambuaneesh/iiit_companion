import os
import random
import subprocess
from app.config import MIN_PORT, MAX_PORT, GENERATED_APPS_DIR
from app.templates.generated_app_template import GENERATED_APP_TEMPLATE

class AppGenerator:
    def generate_app(self, selected_keywords):
        port = self._get_available_port()
        app_dir = os.path.join(GENERATED_APPS_DIR, f"app_{port}")
        os.makedirs(app_dir, exist_ok=True)

        app_content = self._generate_app_content(selected_keywords)
        app_file_path = os.path.join(app_dir, "app.py")

        with open(app_file_path, "w") as f:
            f.write(app_content)

        self._run_app(app_file_path, port)
        return f"http://localhost:{port}"

    def _get_available_port(self):
        return random.randint(MIN_PORT, MAX_PORT)

    def _generate_app_content(self, selected_keywords):
        return GENERATED_APP_TEMPLATE.format(
            environmental=self._get_environmental_content(selected_keywords["Environmental"]),
            resource=self._get_resource_content(selected_keywords["Resource"]),
            academic=self._get_academic_content(selected_keywords["Academic"]),
            event=self._get_event_content(selected_keywords["Event"]),
            health=self._get_health_content(selected_keywords["Health"])
        )

    def _run_app(self, app_file_path, port):
        subprocess.Popen(["streamlit", "run", app_file_path, "--server.port", str(port)])

    # Helper methods for generating content for each microservice
    def _get_environmental_content(self, keywords):
        # Implementation for environmental content
        pass

    def _get_resource_content(self, keywords):
        # Implementation for resource content
        pass

    def _get_academic_content(self, keywords):
        # Implementation for academic content
        pass

    def _get_event_content(self, keywords):
        # Implementation for event content
        pass

    def _get_health_content(self, keywords):
        # Implementation for health content
        pass
