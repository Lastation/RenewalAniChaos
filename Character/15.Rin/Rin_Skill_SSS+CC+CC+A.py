

for i = 0, 9, 1 do

d = 40 + i * 40;
interval = 5 + i * 5;

x = d;
y = 0;

Trigger { -- Skill : Combo
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 2000, " * Devouring One");
      Deaths(CurrentPlayer, Exactly, 140, " `SkillStep");
      Bring(CurrentPlayer, AtLeast, 1, " * Devouring One", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, i * 5, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      CreateUnit(8, "40 + 1n Mojo", "[Skill]Unit_Wait_6", CurrentPlayer);
      CreateUnit(8, "60 + 1n Archon", "[Skill]Unit_Wait_5", CurrentPlayer);
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("15.Rin", " * Devouring One", CurrentPlayer, "Anywhere");
      LMove(165, x, y);
      MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "15.Rin");
      MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "15.Rin");
      LMove(165, -interval, -interval);
      MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "15.Rin");
      MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "15.Rin");
      LMove(165, -interval, -interval);
      MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "15.Rin");
      MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "15.Rin");
      LMove(165, -interval, -interval);
      MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "15.Rin");
      MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "15.Rin");
      LMove(165, -interval, -interval);
      MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "15.Rin");
      MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "15.Rin");
      LMove(165, -interval, -interval);
      MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "15.Rin");
      MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "15.Rin");
      LMove(165, -interval, -interval);
      MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "15.Rin");
      MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "15.Rin");
      LMove(165, -interval, -interval);
      MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "15.Rin");
      MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "15.Rin");
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
   },
}

x = 0;
y = d;

Trigger { -- Skill : Combo
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 2000, " * Devouring One");
      Deaths(CurrentPlayer, Exactly, 140, " `SkillStep");
      Bring(CurrentPlayer, AtLeast, 1, " * Devouring One", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, i * 5 + 1, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      CreateUnit(8, "40 + 1n Mojo", "[Skill]Unit_Wait_6", CurrentPlayer);
      CreateUnit(8, "60 + 1n Archon", "[Skill]Unit_Wait_5", CurrentPlayer);
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("15.Rin", " * Devouring One", CurrentPlayer, "Anywhere");
      LMove(165, x, y);
      MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "15.Rin");
      MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "15.Rin");
      LMove(165, interval, -interval);
      MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "15.Rin");
      MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "15.Rin");
      LMove(165, interval, -interval);
      MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "15.Rin");
      MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "15.Rin");
      LMove(165, interval, -interval);
      MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "15.Rin");
      MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "15.Rin");
      LMove(165, interval, -interval);
      MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "15.Rin");
      MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "15.Rin");
      LMove(165, interval, -interval);
      MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "15.Rin");
      MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "15.Rin");
      LMove(165, interval, -interval);
      MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "15.Rin");
      MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "15.Rin");
      LMove(165, interval, -interval);
      MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "15.Rin");
      MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "15.Rin");
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
   },
}

x = -d;
y = 0;

Trigger { -- Skill : Combo
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 2000, " * Devouring One");
      Deaths(CurrentPlayer, Exactly, 140, " `SkillStep");
      Bring(CurrentPlayer, AtLeast, 1, " * Devouring One", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, i * 5 + 2, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      CreateUnit(8, "40 + 1n Mojo", "[Skill]Unit_Wait_6", CurrentPlayer);
      CreateUnit(8, "60 + 1n Archon", "[Skill]Unit_Wait_5", CurrentPlayer);
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("15.Rin", " * Devouring One", CurrentPlayer, "Anywhere");
      LMove(165, x, y);
      MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "15.Rin");
      MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "15.Rin");
      LMove(165, interval, interval);
      MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "15.Rin");
      MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "15.Rin");
      LMove(165, interval, interval);
      MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "15.Rin");
      MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "15.Rin");
      LMove(165, interval, interval);
      MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "15.Rin");
      MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "15.Rin");
      LMove(165, interval, interval);
      MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "15.Rin");
      MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "15.Rin");
      LMove(165, interval, interval);
      MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "15.Rin");
      MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "15.Rin");
      LMove(165, interval, interval);
      MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "15.Rin");
      MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "15.Rin");
      LMove(165, interval, interval);
      MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "15.Rin");
      MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "15.Rin");
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
   },
}

x = 0;
y = -d;

Trigger { -- Skill : Combo
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 2000, " * Devouring One");
      Deaths(CurrentPlayer, Exactly, 140, " `SkillStep");
      Bring(CurrentPlayer, AtLeast, 1, " * Devouring One", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, i * 5 + 3, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      CreateUnit(8, "40 + 1n Mojo", "[Skill]Unit_Wait_6", CurrentPlayer);
      CreateUnit(8, "60 + 1n Archon", "[Skill]Unit_Wait_5", CurrentPlayer);
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("15.Rin", " * Devouring One", CurrentPlayer, "Anywhere");
      LMove(165, x, y);
      MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "15.Rin");
      MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "15.Rin");
      LMove(165, -interval, interval);
      MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "15.Rin");
      MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "15.Rin");
      LMove(165, -interval, interval);
      MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "15.Rin");
      MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "15.Rin");
      LMove(165, -interval, interval);
      MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "15.Rin");
      MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "15.Rin");
      LMove(165, -interval, interval);
      MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "15.Rin");
      MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "15.Rin");
      LMove(165, -interval, interval);
      MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "15.Rin");
      MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "15.Rin");
      LMove(165, -interval, interval);
      MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "15.Rin");
      MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "15.Rin");
      LMove(165, -interval, interval);
      MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "15.Rin");
      MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "15.Rin");
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
   },
}

Trigger { -- Skill : Combo
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 2000, " * Devouring One");
      Deaths(CurrentPlayer, Exactly, 140, " `SkillStep");
      Bring(CurrentPlayer, AtLeast, 1, " * Devouring One", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, i * 5 + 4, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      KillUnitAt(All, "40 + 1n Mojo", "Anywhere", CurrentPlayer);
      KillUnitAt(All, "60 + 1n Archon", "Anywhere", CurrentPlayer);
      Wait(0);
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
   },
}
end

Trigger { -- Skill : Combo
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 2000, " * Devouring One");
      Deaths(CurrentPlayer, Exactly, 140, " `SkillStep");
      Bring(CurrentPlayer, AtLeast, 1, " * Devouring One", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 50, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      Wait(0);
      SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
      SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
   },
}

d = 320;
interval = 40;

x = d;
y = 0;

Trigger { -- Skill : Combo
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 2000, " * Devouring One");
      Deaths(CurrentPlayer, Exactly, 140, " `SkillStep");
      Bring(CurrentPlayer, AtLeast, 1, " * Devouring One", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 2, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      CreateUnit(2, "60 + 1n Siege", "[Skill]Unit_Wait_6", CurrentPlayer);
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("15.Rin", " * Devouring One", CurrentPlayer, "Anywhere");
      LMove(165, x - 1 * interval, y + 2 * interval);
      MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "15.Rin");
      LMove(165, 0, -4 * interval);
      MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "15.Rin");
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
   },
}

x = 0;
y = d;

Trigger { -- Skill : Combo
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 2000, " * Devouring One");
      Deaths(CurrentPlayer, Exactly, 140, " `SkillStep");
      Bring(CurrentPlayer, AtLeast, 1, " * Devouring One", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 2, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 1, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      CreateUnit(2, "60 + 1n Siege", "[Skill]Unit_Wait_6", CurrentPlayer);
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("15.Rin", " * Devouring One", CurrentPlayer, "Anywhere");
      LMove(165, x - 2 * interval, y - 1 * interval);
      MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "15.Rin");
      LMove(165, 4 * interval, 0);
      MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "15.Rin");
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
   },
}

x = -d;
y = 0;

Trigger { -- Skill : Combo
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 2000, " * Devouring One");
      Deaths(CurrentPlayer, Exactly, 140, " `SkillStep");
      Bring(CurrentPlayer, AtLeast, 1, " * Devouring One", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 2, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 2, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      CreateUnit(2, "60 + 1n Siege", "[Skill]Unit_Wait_6", CurrentPlayer);
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("15.Rin", " * Devouring One", CurrentPlayer, "Anywhere");
      LMove(165, x + 1 * interval, y + 2 * interval);
      MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "15.Rin");
      LMove(165, 0, -4 * interval);
      MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "15.Rin");
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
   },
}

x = 0;
y = -d;

Trigger { -- Skill : Combo
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 2000, " * Devouring One");
      Deaths(CurrentPlayer, Exactly, 140, " `SkillStep");
      Bring(CurrentPlayer, AtLeast, 1, " * Devouring One", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 2, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 3, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      CreateUnit(2, "60 + 1n Siege", "[Skill]Unit_Wait_6", CurrentPlayer);
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("15.Rin", " * Devouring One", CurrentPlayer, "Anywhere");
      LMove(165, x - 2 * interval, y + 1 * interval);
      MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "15.Rin");
      LMove(165, 4 * interval, 0);
      MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "15.Rin");
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
   },
}



Trigger { -- Skill : Combo
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 2000, " * Devouring One");
      Bring(CurrentPlayer, AtLeast, 1, " * Devouring One", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 140, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 2, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 4, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      Wait(6500);
      SetDeaths(CurrentPlayer, SetTo, 0, " `SkillCount");
      SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
      SetDeaths(CurrentPlayer, Add, 12, " `SkillWait");
   },
}