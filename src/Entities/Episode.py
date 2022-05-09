class Episode:
  def __init__(self, episode: tuple) -> None:
    self.episode_id = episode[0]
    self.series_id = episode[1]
    self.series_name = episode[2]
    self.season = episode[3]
    self.title = episode[4]
    self.data_aired = episode[5]
    self.run_time = episode[6]
    self.monster_real = episode[7]
    self.motive = episode[8]