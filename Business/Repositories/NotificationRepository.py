from Data.Persistance.database import *
from Data.Domain.Notification import Notification


class NotificationRepository:
    db_context = db_session

    def create_notification_for_user(self, user_id, message):
        notification = Notification()

        notification.user_id = user_id
        notification.content = message
        try:
            self.db_context.add(notification)
            self.db_context.commit()
        except:
            pass
