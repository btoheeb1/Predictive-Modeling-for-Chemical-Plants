

from numpy.typing import NDArray


class DataScaler:

    __slots__ = ('data', '_scaler')


    def __init__(self, data:NDArray) -> None:
        self.data=data
        self._scale_data()

    def _scale_data(self)-> None:
        from sklearn.preprocessing import RobustScaler

        self._scaler = RobustScaler()
        self._scaler.fit(self.data)

    def get_transformed_data(self)->NDArray:
        return self._scaler.transform(self.data)

    