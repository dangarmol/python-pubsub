# -*- coding: utf-8 -*-
# Copyright 2024 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
from typing import Union

from .pubsub import (
    AcknowledgeRequest,
    BigQueryConfig,
    CloudStorageConfig,
    CreateSnapshotRequest,
    DeadLetterPolicy,
    DeleteSnapshotRequest,
    DeleteSubscriptionRequest,
    DeleteTopicRequest,
    DetachSubscriptionRequest,
    DetachSubscriptionResponse,
    ExpirationPolicy,
    GetSnapshotRequest,
    GetSubscriptionRequest,
    GetTopicRequest,
    IngestionDataSourceSettings,
    ListSnapshotsRequest,
    ListSnapshotsResponse,
    ListSubscriptionsRequest,
    ListSubscriptionsResponse,
    ListTopicSnapshotsRequest,
    ListTopicSnapshotsResponse,
    ListTopicsRequest,
    ListTopicsResponse,
    ListTopicSubscriptionsRequest,
    ListTopicSubscriptionsResponse,
    MessageStoragePolicy,
    ModifyAckDeadlineRequest,
    ModifyPushConfigRequest,
    PlatformLogsSettings,
    PublishRequest,
    PublishResponse,
    PubsubMessage,
    PullRequest,
    PullResponse,
    PushConfig,
    ReceivedMessage,
    RetryPolicy,
    SchemaSettings,
    SeekRequest,
    SeekResponse,
    Snapshot,
    StreamingPullRequest,
    StreamingPullResponse,
    Subscription,
    Topic,
    UpdateSnapshotRequest,
    UpdateSubscriptionRequest,
    UpdateTopicRequest,
)
from .schema import (
    CommitSchemaRequest,
    CreateSchemaRequest,
    DeleteSchemaRequest,
    DeleteSchemaRevisionRequest,
    GetSchemaRequest,
    ListSchemaRevisionsRequest,
    ListSchemaRevisionsResponse,
    ListSchemasRequest,
    ListSchemasResponse,
    RollbackSchemaRequest,
    Schema,
    ValidateMessageRequest,
    ValidateMessageResponse,
    ValidateSchemaRequest,
    ValidateSchemaResponse,
    Encoding,
    SchemaView,
)

TimeoutType = Union[
    int,
    float,
    "google.api_core.timeout.ConstantTimeout",
    "google.api_core.timeout.ExponentialTimeout",
]
"""The type of the timeout parameter of publisher client methods."""

__all__ = (
    "TimeoutType",
    "AcknowledgeRequest",
    "BigQueryConfig",
    "CloudStorageConfig",
    "CreateSnapshotRequest",
    "DeadLetterPolicy",
    "DeleteSnapshotRequest",
    "DeleteSubscriptionRequest",
    "DeleteTopicRequest",
    "DetachSubscriptionRequest",
    "DetachSubscriptionResponse",
    "ExpirationPolicy",
    "GetSnapshotRequest",
    "GetSubscriptionRequest",
    "GetTopicRequest",
    "IngestionDataSourceSettings",
    "ListSnapshotsRequest",
    "ListSnapshotsResponse",
    "ListSubscriptionsRequest",
    "ListSubscriptionsResponse",
    "ListTopicSnapshotsRequest",
    "ListTopicSnapshotsResponse",
    "ListTopicsRequest",
    "ListTopicsResponse",
    "ListTopicSubscriptionsRequest",
    "ListTopicSubscriptionsResponse",
    "MessageStoragePolicy",
    "ModifyAckDeadlineRequest",
    "ModifyPushConfigRequest",
    "PlatformLogsSettings",
    "PublishRequest",
    "PublishResponse",
    "PubsubMessage",
    "PullRequest",
    "PullResponse",
    "PushConfig",
    "ReceivedMessage",
    "RetryPolicy",
    "SchemaSettings",
    "SeekRequest",
    "SeekResponse",
    "Snapshot",
    "StreamingPullRequest",
    "StreamingPullResponse",
    "Subscription",
    "Topic",
    "UpdateSnapshotRequest",
    "UpdateSubscriptionRequest",
    "UpdateTopicRequest",
    "CommitSchemaRequest",
    "CreateSchemaRequest",
    "DeleteSchemaRequest",
    "DeleteSchemaRevisionRequest",
    "GetSchemaRequest",
    "ListSchemaRevisionsRequest",
    "ListSchemaRevisionsResponse",
    "ListSchemasRequest",
    "ListSchemasResponse",
    "RollbackSchemaRequest",
    "Schema",
    "ValidateMessageRequest",
    "ValidateMessageResponse",
    "ValidateSchemaRequest",
    "ValidateSchemaResponse",
    "Encoding",
    "SchemaView",
)
