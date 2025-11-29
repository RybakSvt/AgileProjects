__all__ = [
    'TagSerializer',
    'ProjectDetailSerializer',
    'AllTasksSerializer',
    'CreateTaskSerializer',
]



from .tag_serializers import TagSerializer
from .project_serializers import ProjectDetailSerializer
from .task_serializers import (
    AllTasksSerializer,
    CreateTaskSerializer
)
