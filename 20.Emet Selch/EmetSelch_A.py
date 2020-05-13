

for i = 0, 3, 1 do

radius = i / 4 * math.pi;

d = 50;
interval = 50;

i_x = math.sin(radius) * interval;
i_y = math.cos(radius) * interval;
i_x = math.floor(i_x + 0.5);
i_y = math.floor(i_y + 0.5);

x1 = math.sin(radius) * interval - i_y;
y1 = math.cos(radius) * interval + i_x;
x1 = math.floor(x1 + 0.5);
y1 = math.floor(y1 + 0.5);

x2 = math.sin(radius) * interval + i_y;
y2 = math.cos(radius) * interval - i_x;
x2 = math.floor(x2 + 0.5);
y2 = math.floor(y2 + 0.5);


Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 3000, " * Samir Duran");
      Bring(CurrentPlayer, AtLeast, 1, " * Samir Duran", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 300, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, i, " `SkillLoop");
      Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
   },
   actions = {
      Comment("Skill : A");
      PreserveTrigger();
      CreateUnit(4, "40 + 1n Zergling", "[Skill]Unit_Wait_8", CurrentPlayer);  
      CreateUnit(4, "40 + 1n Guardian", "[Skill]Unit_Wait_8", CurrentPlayer);  
      CreateUnit(4, " Unit. Hoffnung 25000", "[Skill]Unit_Wait_8", CurrentPlayer);  
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("20.EmetSelch", " * Samir Duran", CurrentPlayer, "Anywhere");
      LMove(175, x1, y1);
      MoveUnit(1, "40 + 1n Zergling", CurrentPlayer, "[Skill]Unit_Wait_ALL", "20.EmetSelch");
      MoveUnit(1, "40 + 1n Guardian", CurrentPlayer, "[Skill]Unit_Wait_ALL", "20.EmetSelch");
      LMove(175, i_x, i_y);
      MoveUnit(1, " Unit. Hoffnung 25000", CurrentPlayer, "[Skill]Unit_Wait_ALL", "20.EmetSelch");
      MoveLocation("20.EmetSelch", " * Samir Duran", CurrentPlayer, "Anywhere");
      LMove(175, x2, y2);
      MoveUnit(1, "40 + 1n Zergling", CurrentPlayer, "[Skill]Unit_Wait_ALL", "20.EmetSelch");
      MoveUnit(1, "40 + 1n Guardian", CurrentPlayer, "[Skill]Unit_Wait_ALL", "20.EmetSelch");
      LMove(175, i_x, i_y);
      MoveUnit(1, " Unit. Hoffnung 25000", CurrentPlayer, "[Skill]Unit_Wait_ALL", "20.EmetSelch");
      MoveLocation("20.EmetSelch", " * Samir Duran", CurrentPlayer, "Anywhere");
      LMove(175, -x1, -y1);
      MoveUnit(1, "40 + 1n Zergling", CurrentPlayer, "[Skill]Unit_Wait_ALL", "20.EmetSelch");
      MoveUnit(1, "40 + 1n Guardian", CurrentPlayer, "[Skill]Unit_Wait_ALL", "20.EmetSelch");
      LMove(175, -i_x, -i_y);
      MoveUnit(1, " Unit. Hoffnung 25000", CurrentPlayer, "[Skill]Unit_Wait_ALL", "20.EmetSelch");
      MoveLocation("20.EmetSelch", " * Samir Duran", CurrentPlayer, "Anywhere");
      LMove(175, -x2, -y2);
      MoveUnit(1, "40 + 1n Zergling", CurrentPlayer, "[Skill]Unit_Wait_ALL", "20.EmetSelch");
      MoveUnit(1, "40 + 1n Guardian", CurrentPlayer, "[Skill]Unit_Wait_ALL", "20.EmetSelch");
      LMove(175, -i_x, -i_y);
      MoveUnit(1, " Unit. Hoffnung 25000", CurrentPlayer, "[Skill]Unit_Wait_ALL", "20.EmetSelch");
      MoveLocation("20.EmetSelch", " * Samir Duran", CurrentPlayer, "Anywhere");
      Order("40 + 1n Zergling", CurrentPlayer, "Anywhere", Attack, "20.EmetSelch");
      KillUnitAt(All, "40 + 1n Guardian", "Anywhere", CurrentPlayer);
      KillUnitAt(All, " Unit. Hoffnung 25000", "Anywhere", CurrentPlayer);
      Wait(120);
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
   },
}

end

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 3000, " * Samir Duran");
      Bring(CurrentPlayer, AtLeast, 1, " * Samir Duran", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 300, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 4, " `SkillLoop");
   },
   actions = {
      Comment("Skill : A");
      PreserveTrigger();
      Wait(600);
      KillUnitAt(All, "40 + 1n Zergling", "Anywhere", CurrentPlayer);
      Wait(500);
      SetDeaths(CurrentPlayer, SetTo, 0, " `SkillCount");
      SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
      SetDeaths(CurrentPlayer, Add, 12, " `SkillWait");
   },
}