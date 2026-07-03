class StateTransitionViolationMatrix:
    """
    Computes trajectory vectors to flag wrong-way violations
    and tracking continuities across multi-class scenarios.
    """

    def __init__(self, tracking_threshold=0.85):
        self.tracking_threshold = tracking_threshold

    def evaluate_state_transition(self, historical_track, current_bbox):
        """
        Evaluates current bounding box trajectory against target transition models.
        """
        if not historical_track:
            return "STATE_INITIALIZING"

        last_x, last_y = historical_track[-1]
        curr_x, curr_y = current_bbox[0], current_bbox[1]

        # Heading delta vector calculations
        delta_y = curr_y - last_y

        if delta_y < -5.0:  # Arbitrary coordinate threshold representing opposing heading
            return "VIOLATION_WRONG_WAY"
        return "STATE_NOMINAL"