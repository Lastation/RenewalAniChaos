

for i = 0, 3, 1 do

radius = 0 / 4 * math.pi;

d = 90;

x = math.sin(radius) * d;
y = math.cos(radius) * d;
x = math.floor(x + 0.5);
y = math.floor(y + 0.5);


Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 3000, " * Samir Duran");
      Bring(CurrentPlayer, AtLeast, 1, " * Samir Duran", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 110, " `SkillStep");
      Deaths(CurrentPlayer, AtMost, 3, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, i, " `SkillLoop");
      Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      CreateUnit(2, "40 + 1n Goliath", "[Skill]Unit_Wait_8", CurrentPlayer);  
      CreateUnit(4, "40 + 1n Mutalisk", "[Skill]Unit_Wait_8", CurrentPlayer);  
      CreateUnit(28, " Creep. Dunkelheit", "[Skill]Unit_Wait_3", CurrentPlayer);  
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("20.EmetSelch", " * Samir Duran", CurrentPlayer, "Anywhere");
      LMove(175, x, y);
      MoveUnit(1, "40 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "20.EmetSelch");
      MoveUnit(1, "40 + 1n Mutalisk", CurrentPlayer, "[Skill]Unit_Wait_ALL", "20.EmetSelch");
      MoveUnit(7, " Creep. Dunkelheit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "20.EmetSelch");
      MoveLocation("20.EmetSelch", " * Samir Duran", CurrentPlayer, "Anywhere");
      LMove(175, -x, -y);
      MoveUnit(1, "40 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "20.EmetSelch");
      MoveUnit(1, "40 + 1n Mutalisk", CurrentPlayer, "[Skill]Unit_Wait_ALL", "20.EmetSelch");
      MoveUnit(7, " Creep. Dunkelheit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "20.EmetSelch");
      MoveLocation("20.EmetSelch", " * Samir Duran", CurrentPlayer, "Anywhere");
      LMove(175, -y, x);
      MoveUnit(1, "40 + 1n Mutalisk", CurrentPlayer, "[Skill]Unit_Wait_ALL", "20.EmetSelch");
      MoveUnit(7, " Creep. Dunkelheit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "20.EmetSelch");
      MoveLocation("20.EmetSelch", " * Samir Duran", CurrentPlayer, "Anywhere");
      LMove(175, y, -x);
      MoveUnit(1, "40 + 1n Mutalisk", CurrentPlayer, "[Skill]Unit_Wait_ALL", "20.EmetSelch");
      MoveUnit(7, " Creep. Dunkelheit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "20.EmetSelch");
      MoveLocation("20.EmetSelch", " * Samir Duran", CurrentPlayer, "Anywhere");
      MoveUnit(All, "40 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "20.EmetSelch");
      Order("40 + 1n Goliath", CurrentPlayer, "Anywhere", Attack, "20.EmetSelch");
      KillUnitAt(All, "40 + 1n Mutalisk", "Anywhere", CurrentPlayer);
      KillUnitAt(All, " Creep. Dunkelheit", "Anywhere", CurrentPlayer);
      Wait(0);
      RemoveUnitAt(All, "40 + 1n Goliath", "Anywhere", CurrentPlayer);
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
   },
}

end


Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 3000, " * Samir Duran");
      Bring(CurrentPlayer, AtLeast, 1, " * Samir Duran", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 110, " `SkillStep");
      Deaths(CurrentPlayer, AtMost, 3, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 4, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      Wait(750);
      SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
      SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
   },
}

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 3000, " * Samir Duran");
      Bring(CurrentPlayer, AtLeast, 1, " * Samir Duran", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 110, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 4, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      Wait(1000);
      SetDeaths(AllPlayers, SetTo, 2001, " `SkillText4");
      SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
      SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
   },
}


for i = 0, 3, 1 do

radius = 1 / 4 * math.pi;

d = 120;

x = math.sin(radius) * d;
y = math.cos(radius) * d;
x = math.floor(x + 0.5);
y = math.floor(y + 0.5);


Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 3000, " * Samir Duran");
      Bring(CurrentPlayer, AtLeast, 1, " * Samir Duran", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 110, " `SkillStep");
      Deaths(CurrentPlayer, AtLeast, 5, " `SkillCount");
      Deaths(CurrentPlayer, AtMost, 7, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, i, " `SkillLoop");
      Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      CreateUnit(2, "40 + 1n Goliath", "[Skill]Unit_Wait_8", CurrentPlayer);  
      CreateUnit(4, "40 + 1n Guardian", "[Skill]Unit_Wait_8", CurrentPlayer);  
      CreateUnit(28, " Creep. Dunkelheit", "[Skill]Unit_Wait_3", CurrentPlayer);  
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("20.EmetSelch", " * Samir Duran", CurrentPlayer, "Anywhere");
      LMove(175, x, y);
      MoveUnit(1, "40 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "20.EmetSelch");
      MoveUnit(1, "40 + 1n Guardian", CurrentPlayer, "[Skill]Unit_Wait_ALL", "20.EmetSelch");
      MoveUnit(7, " Creep. Dunkelheit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "20.EmetSelch");
      MoveLocation("20.EmetSelch", " * Samir Duran", CurrentPlayer, "Anywhere");
      LMove(175, -x, -y);
      MoveUnit(1, "40 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "20.EmetSelch");
      MoveUnit(1, "40 + 1n Guardian", CurrentPlayer, "[Skill]Unit_Wait_ALL", "20.EmetSelch");
      MoveUnit(7, " Creep. Dunkelheit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "20.EmetSelch");
      MoveLocation("20.EmetSelch", " * Samir Duran", CurrentPlayer, "Anywhere");
      LMove(175, -y, x);
      MoveUnit(1, "40 + 1n Guardian", CurrentPlayer, "[Skill]Unit_Wait_ALL", "20.EmetSelch");
      MoveUnit(7, " Creep. Dunkelheit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "20.EmetSelch");
      MoveLocation("20.EmetSelch", " * Samir Duran", CurrentPlayer, "Anywhere");
      LMove(175, y, -x);
      MoveUnit(1, "40 + 1n Guardian", CurrentPlayer, "[Skill]Unit_Wait_ALL", "20.EmetSelch");
      MoveUnit(7, " Creep. Dunkelheit", CurrentPlayer, "[Skill]Unit_Wait_ALL", "20.EmetSelch");
      MoveLocation("20.EmetSelch", " * Samir Duran", CurrentPlayer, "Anywhere");
      MoveUnit(All, "40 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "20.EmetSelch");
      Order("40 + 1n Goliath", CurrentPlayer, "Anywhere", Attack, "20.EmetSelch");
      KillUnitAt(All, "40 + 1n Guardian", "Anywhere", CurrentPlayer);
      KillUnitAt(All, " Creep. Dunkelheit", "Anywhere", CurrentPlayer);
      Wait(0);
      RemoveUnitAt(All, "40 + 1n Goliath", "Anywhere", CurrentPlayer);
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
   },
}

end


Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 3000, " * Samir Duran");
      Bring(CurrentPlayer, AtLeast, 1, " * Samir Duran", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 110, " `SkillStep");
      Deaths(CurrentPlayer, AtLeast, 5, " `SkillCount");
      Deaths(CurrentPlayer, AtMost, 7, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 4, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      Wait(750);
      SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
      SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
   },
}


Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 3000, " * Samir Duran");
      Bring(CurrentPlayer, AtLeast, 1, " * Samir Duran", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 110, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 8, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      Wait(500);
      SetDeaths(CurrentPlayer, SetTo, 0, " `SkillCount");
      SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
      SetDeaths(CurrentPlayer, Add, 12, " `SkillWait");
   },
}