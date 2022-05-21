class Culprit:
  def __init__(self, culprit_id: str = '', culprit_name: str = '', culprit_gender: str = '') -> None:
    self.culprit_id = culprit_id
    self.culprit_name = culprit_name
    self.culprit_gender = culprit_gender
        
class Monster:
  def __init__(self, monster_id: str = '', monster_name: str = '', monster_gender: str = '', monster_type: str = '', monster_species: str = '', monster_subtype: str = '') -> None:
    self.monster_id = monster_id
    self.monster_name = monster_name
    self.monster_gender = monster_gender
    self.monster_type = monster_type
    self.monster_species = monster_species
    self.monster_subtype = monster_subtype
          
class VoiceActor:
  def __init__(self, actor_id: int = -1, character_name: str = '', actor_name: str = '') -> None:
    self.actor_id = actor_id
    self.character_name = character_name
    self.actor_name = actor_name
    
class Episode:
  def __init__(self, episode_id: int = -1, setting_id: int = -1, series_name: str = '', season: int = 0, title: str = '', date_aired: str = '', runtime: int = 0, monster_real: str = '', motive: str = '') -> None:
    self.episode_id = episode_id
    self.setting_id = setting_id
    self.series_name = series_name
    self.season = season
    self.title = title
    self.date_aired = date_aired
    self.runtime = runtime
    self.monster_real = monster_real
    self.motive = motive
      
class Setting:
  def __init__(self, setting_terrain: str = '', setting_place: str = '') -> None:
    self.setting_terrain = setting_terrain
    self.setting_place = setting_place