from app.dependencies.db.db_session_dep import DBSessionDep


class AdminOrdersController:
    def __init__(self, db_session: DBSessionDep):
        self.db_session = db_session

    def get_orders(
        self,
        page: int,
        limit: int,
    ):
        pass
