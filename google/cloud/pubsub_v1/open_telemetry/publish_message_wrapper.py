import sys
from datetime import datetime

from google.pubsub_v1 import types as gapic_types
from opentelemetry import trace


class PublishMessageWrapper:
    _OPEN_TELEMETRY_TRACER_NAME: str = "google.cloud.pubsub_v1.publisher"
    _OPEN_TELEMETRY_MESSAGING_SYSTEM: str = "gcp_pubsub"

    _PUBLISH_START_EVENT: str = "publish start"

    def __init__(self, message: gapic_types.PubsubMessage):
        self._message: gapic_types.PubsubMessage = message

    def start_create_span(self, topic: str, ordering_key: str) -> trace.Span:
        tracer = trace.get_tracer(self._OPEN_TELEMETRY_TRACER_NAME)
        with tracer.start_as_current_span(
            name=f"{topic} create",
            attributes={
                "messaging.system": self._OPEN_TELEMETRY_MESSAGING_SYSTEM,
                "messaging.destination.name": topic,
                "code.function": "google.cloud.pubsub.PublisherClient.publish",
                "messaging.gcp_pubsub.message.ordering_key": ordering_key,
                "messaging.operation": "create",
                "gcp.project_id": topic.split("/")[1],
                "messaging.message.body.size": sys.getsizeof(self._message.data),
            },
            kind=trace.SpanKind.PRODUCER,
            end_on_exit=False,
        ) as create_span:
            create_span.add_event(
                name=self._PUBLISH_START_EVENT,
                attributes={
                    "timestamp": str(datetime.now()),
                },
            )
            return create_span
