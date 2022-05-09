class Episode:
  def __init__(self, actor: tuple) -> None:
    self.actor_id = actor[0]
    self.character_name = actor[1]
    self.actor_name = actor[2]