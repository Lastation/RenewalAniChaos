
x = 50;
y = 50;

for i = 0, 3, 1 do

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 1000, " * Probe");
      Bring(CurrentPlayer, AtLeast, 1, " * Probe", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 100, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, i, " `SkillLoop");
      Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
   },
   actions = {
      Comment("Skill : S");
      PreserveTrigger();
      CreateUnit(4, "40 + 1n Goliath", "[Skill]Unit_Wait_8", CurrentPlayer);  
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("21. Magellan", " * Probe", CurrentPlayer, "Anywhere");
      LMove(178, x, y);
      MoveUnit(1, "40 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "21. Magellan");
      MoveLocation("21. Magellan", " * Probe", CurrentPlayer, "Anywhere");
      LMove(178, -x, -y);
      MoveUnit(1, "40 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "21. Magellan");
      MoveLocation("21. Magellan", " * Probe", CurrentPlayer, "Anywhere");
      LMove(178, -y, x);
      MoveUnit(1, "40 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "21. Magellan");
      MoveLocation("21. Magellan", " * Probe", CurrentPlayer, "Anywhere");
      LMove(178, y, -x);
      MoveUnit(1, "40 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "21. Magellan");
      MoveLocation("21. Magellan", " * Probe", CurrentPlayer, "Anywhere");
      MoveUnit(All, "40 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "21. Magellan");
      Order("40 + 1n Goliath", CurrentPlayer, "Anywhere", Attack, "21. Magellan");
      Wait(160);
      KillUnitAt(All, "40 + 1n Goliath", "Anywhere", CurrentPlayer);
      Wait(0);
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
   },
}

end


Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 1000, " * Probe");
      Bring(CurrentPlayer, AtLeast, 1, " * Probe", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 100, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 4, " `SkillLoop");
   },
   actions = {
      Comment("Skill : S");
      PreserveTrigger();
      Wait(500);
      SetDeaths(CurrentPlayer, SetTo, 0, " `SkillCount");
      SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
      SetDeaths(CurrentPlayer, Add, 12, " `SkillWait");
   },
}