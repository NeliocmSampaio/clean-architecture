from domain.__seedwork.use_case_interface import UseCaseInterface
from domain.user.user_repository_interface import UserRepositoryInterface
from usecases.user.list_users.list_users_dto import ListUsersInputDto, ListUsersOutputDto, UserDto


class ListUsersUseCase(UseCaseInterface):
    user_repository: UserRepositoryInterface

    def __init__(self, user_repository: UserRepositoryInterface):
        self.user_repository = user_repository

    def execute(self, input: ListUsersInputDto) -> ListUsersOutputDto:
        users = self.user_repository.list_users()

        output = []
        for user in users:
            user_dto = UserDto(id= user.id, name=user.name)

            output.append(user_dto)
        
        return ListUsersOutputDto(users=output)