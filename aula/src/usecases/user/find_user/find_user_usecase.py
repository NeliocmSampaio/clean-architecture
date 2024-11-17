from domain.__seedwork.user_case_interface import UseCaseInterface
from domain.user.user_repository_interface import UserRepositoryInterface
from usecases.user.find_user.find_user_dto import FindUserInputDto, FindUserOutpudDto


class FindUserUseCase(UseCaseInterface):

    user_repository: UserRepositoryInterface

    def __init__(self, user_repository: UserRepositoryInterface):
        self.user_repository = user_repository

    def execute(self, input: FindUserInputDto) -> FindUserOutpudDto:
        user = self.user_repository.find_user(user_id=input.id)
        return FindUserInputDto(
            id=user.id,
            name=user.name
        )
