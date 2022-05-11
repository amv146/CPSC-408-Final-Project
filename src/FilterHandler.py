from Filters import *
from GUI.Menu import Menu
 
class FilterHandler:
  def __init__(self, database: ScoobyDooDatabase):
    self.filter_dict: dict[FilterType, Filter] = filter_dict

    self.database: ScoobyDooDatabase = database
    self.filters = list(filter_dict.values())
    self.__update_filters__()
    
      
  def __on_select__(self, menu: Menu):
    self.change_filter_value( menu.filter_type, menu.options.get())
    print(menu.filter_type)
    for menu2 in self.menus:
  
      if (menu.options.get() == ' ' or menu.options.get() == '') or menu2 != menu:
        menu2.add_options()

  def change_filter_value(self, filter_type: FilterType, value: str):
    print(value)
    self.filter_dict[filter_type].applied_value = value
    self.__update_filters__()
    # print(self.filter_dict[FilterType.SEASON])
  
  def __update_filters__(self):
    df = self.__get_options_df__()
    for filter in self.filters:
      self.__update_filter__(df, filter)
  
  def __get_options_df__(self) -> DataFrame:
    series_name = self.__get_value__(self.filter_dict[FilterType.SERIES_NAME].applied_value)
    if (self.filter_dict[FilterType.SEASON].applied_value != ' '):
      season = int(self.filter_dict[FilterType.SEASON].applied_value or 0)
    else:
      season = 0    
    date_aired = self.__get_value__(self.filter_dict[FilterType.DATE_AIRED].applied_value)
    setting_terrain = self.__get_value__(self.filter_dict[FilterType.SETTING_TERRAIN].applied_value)
    setting_place = self.__get_value__(self.filter_dict[FilterType.SETTING_PLACE].applied_value)
    actor_name = self.__get_value__(self.filter_dict[FilterType.ACTOR_NAME].applied_value)
    character_name = self.__get_value__(self.filter_dict[FilterType.CHARACTER_NAME].applied_value)
    monster_name = self.__get_value__(self.filter_dict[FilterType.MONSTER_NAME].applied_value)
    monster_gender = self.__get_value__(self.filter_dict[FilterType.MONSTER_GENDER].applied_value)
    monster_species = self.__get_value__(self.filter_dict[FilterType.MONSTER_SPECIES].applied_value)
    culprit_name = self.__get_value__(self.filter_dict[FilterType.CULPRIT_NAME].applied_value)
    culprit_gender = self.__get_value__(self.filter_dict[FilterType.CULPRIT_GENDER].applied_value)
    return self.database.run_all_procedure(series_name = series_name, season = season, title = '', date_aired = date_aired, runtime = 0, monster_real = '', motive = '', 
                                    setting_terrain = setting_terrain, setting_place = setting_place, 
                                    actor_name = actor_name, character_name = character_name, 
                                    monster_name = monster_name, monster_gender = monster_gender, monster_type = '', monster_species = monster_species, monster_subtype = '', 
                                    culprit_name = culprit_name, culprit_gender = culprit_gender)
    
  def __get_value__(self, string):
    if string == ' ' or 0 or '':
      return ''
    return string
    
  def __update_filter__(self, df: DataFrame, filter: Filter):
    filter_name = str(filter.type)
    filter.options = list(df[filter_name].drop_duplicates().dropna())
    
  def get_options(self, filter_type: FilterType) -> list[str]:
    return self.filter_dict[filter_type].options
  
  def get_applied_value(self, filter_type: FilterType) -> str: 
    return self.filter_dict[filter_type].applied_value

