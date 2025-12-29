import reflex as rx

from .data.airport_list import AIRPORT_CODE_SET


class RouteState(rx.State):
    source_airport: str = ""
    dest_airport: str = ""
    months_back: int = 3

    @rx.event
    def set_months_back(self, months: int):
        self.months_back = max(1, int(months))

    # this method isn't an event so don't use the event decorator
    def _norm_code(self, value: str) -> str:
        v = (value or "").upper().strip()
        return v[:3]

    @rx.event
    def set_source_airport(self, value: str):
        v = self._norm_code(value)
        self.source_airport = v

        if len(v) == 3 and v not in AIRPORT_CODE_SET:
            # self.source_airport = ""
            yield rx.toast.error("Unknown origin airport code. Pick one from the list.")
            return

    @rx.event
    def set_dest_airport(self, value: str):
        v = self._norm_code(value)
        self.dest_airport = v

        if len(v) == 3 and v not in AIRPORT_CODE_SET:
            # self.dest_airport = ""
            yield rx.toast.error(
                "Unknown destination airport code. Pick one from the list."
            )
            return

    @rx.event
    def analyze(self):

        if not self.source_airport or not self.dest_airport:
            yield rx.toast.warning(
                "Enter both origin and destination before analyzing."
            )
            return

        if (self.source_airport not in AIRPORT_CODE_SET) or (
            self.dest_airport not in AIRPORT_CODE_SET
        ):
            yield rx.toast.error("Please select valid airport codes from the list.")
            return

            # defensive checks (when both origin = destination)
        if (
            (self.source_airport in AIRPORT_CODE_SET)
            and (self.dest_airport in AIRPORT_CODE_SET)
            and (self.source_airport == self.dest_airport)
        ):
            yield rx.toast.error("Origin and destination cannot be the same.")
            return

        ### method to trigger analysis pipeline starts here

        # bring in the data from user input
        yield rx.console_log(self.source_airport)

        yield rx.console_log(self.dest_airport)

        yield rx.console_log(str(self.months_back))
