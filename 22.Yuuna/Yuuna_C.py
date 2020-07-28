
for i = 0, 2, 1 do

radius = 1 / 4 * math.pi;

d = 50;

x = math.sin(radius) * d;
y = math.cos(radius) * d;
x = math.floor(x + 0.5);
y = math.floor(y + 0.5);

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 3000, " * Devouring One");
      Bring(CurrentPlayer, AtLeast, 1, " * Devouring One", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 200, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 2 * i, " `SkillLoop");
      Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
   },
   actions = {
      Comment("Skill : C");
      PreserveTrigger();
      CreateUnit(5, "Protoss Observer", "[Skill]Unit_Wait_8", CurrentPlayer);  
      CreateUnit(4, "40 + 1n Goliath", "[Skill]Unit_Wait_8", CurrentPlayer);  
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("22.Yuuna", " * Devouring One", CurrentPlayer, "Anywhere");
      LMove(181, x, y);
      MoveUnit(1, "40 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      MoveUnit(1, "Protoss Observer", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      MoveLocation("22.Yuuna", " * Devouring One", CurrentPlayer, "Anywhere");
      LMove(181, -x, -y);
      MoveUnit(1, "40 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      MoveUnit(1, "Protoss Observer", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      MoveLocation("22.Yuuna", " * Devouring One", CurrentPlayer, "Anywhere");
      LMove(181, -y, x);
      MoveUnit(1, "40 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      MoveUnit(1, "Protoss Observer", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      MoveLocation("22.Yuuna", " * Devouring One", CurrentPlayer, "Anywhere");
      LMove(181, y, -x);
      MoveUnit(1, "40 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      MoveUnit(1, "Protoss Observer", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      MoveLocation("22.Yuuna", " * Devouring One", CurrentPlayer, "Anywhere");
      MoveUnit(1, "Protoss Observer", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
   },
}

radius = 0 / 4 * math.pi;

d = 50;

x = math.sin(radius) * d;
y = math.cos(radius) * d;
x = math.floor(x + 0.5);
y = math.floor(y + 0.5);

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 3000, " * Devouring One");
      Bring(CurrentPlayer, AtLeast, 1, " * Devouring One", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 200, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 2 * i + 1, " `SkillLoop");
   },
   actions = {
      Comment("Skill : C");
      PreserveTrigger();
      CreateUnit(4, "Protoss Observer", "[Skill]Unit_Wait_8", CurrentPlayer);  
      CreateUnit(4, "40 + 1n Goliath", "[Skill]Unit_Wait_8", CurrentPlayer);  
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("22.Yuuna", " * Devouring One", CurrentPlayer, "Anywhere");
      LMove(181, x, y);
      MoveUnit(1, "40 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      MoveUnit(1, "Protoss Observer", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      MoveLocation("22.Yuuna", " * Devouring One", CurrentPlayer, "Anywhere");
      LMove(181, -x, -y);
      MoveUnit(1, "40 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      MoveUnit(1, "Protoss Observer", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      MoveLocation("22.Yuuna", " * Devouring One", CurrentPlayer, "Anywhere");
      LMove(181, -y, x);
      MoveUnit(1, "40 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      MoveUnit(1, "Protoss Observer", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      MoveLocation("22.Yuuna", " * Devouring One", CurrentPlayer, "Anywhere");
      LMove(181, y, -x);
      MoveUnit(1, "40 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      MoveUnit(1, "Protoss Observer", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      KillUnitAt(All, "Protoss Observer", "Anywhere", CurrentPlayer);
      MoveLocation("22.Yuuna", " * Devouring One", CurrentPlayer, "Anywhere");
      MoveUnit(All, "40 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "22.Yuuna");
      Order("40 + 1n Goliath", CurrentPlayer, "Anywhere", Attack, "22.Yuuna");
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
      Deaths(CurrentPlayer, Exactly, 3000, " * Devouring One");
      Bring(CurrentPlayer, AtLeast, 1, " * Devouring One", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 200, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 6, " `SkillLoop");
   },
   actions = {
      Comment("Skill : C");
      PreserveTrigger();
      Wait(500);
      SetDeaths(CurrentPlayer, SetTo, 0, " `SkillCount");
      SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
      SetDeaths(CurrentPlayer, Add, 12, " `SkillWait");
   },
}