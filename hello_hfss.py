import hycohanz as hfss

[oAnsoftApp, oDesktop]=hfss.setup_interface()
oProject = hfss.new_project(oDesktop)

oDesign = hfss.insert_design(oProject, 'Design2', 'DrivenModal')

hfss.add_property(oDesign,'a','10mil')

hfss.open_project(oDesktop,'C:\Users\TY\Documents\Ansoft\cavity.hfss')

oProject=hfss.get_active_project(oDesktop)

#hfss.close_current_project(oDesktop)

hfss.close_all_projects_except_current(oDesktop)

design_list=hfss.get_top_design_list(oProject)

oDesign=hfss.get_design(oProject, design_list[1])

Project_name=hfss.get_project_name(oProject)

oDesign.Analyze('Setup1, Sweep')

