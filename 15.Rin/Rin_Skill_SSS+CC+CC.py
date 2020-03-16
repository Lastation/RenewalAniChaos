radius = 1 / 8 * math.pi;

d = 70;

x = math.sin(radius) * d;
y = math.cos(radius) * d;
x = math.floor(x + 0.5);
y = math.floor(y + 0.5);

Trigger { -- Skill : Combo
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 2000, " * Devouring One");
      Deaths(CurrentPlayer, Exactly, 130, " `SkillStep");
      Bring(CurrentPlayer, AtLeast, 1, " * Devouring One", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      CreateUnit(32, " Unit. Schnee", "[Skill]Unit_Wait_1", CurrentPlayer);
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("15.Rin", " * Devouring One", CurrentPlayer, "Anywhere");
      LMove(165, x, y);
      MoveUnit(16, " Unit. Schnee", CurrentPlayer, "[Skill]Unit_Wait_ALL", "15.Rin");
      MoveLocation("15.Rin", " * Devouring One", CurrentPlayer, "Anywhere");
      LMove(165, -x, -y);
      MoveUnit(16, " Unit. Schnee", CurrentPlayer, "[Skill]Unit_Wait_ALL", "15.Rin");
      CreateUnit(32, " Unit. Schnee", "[Skill]Unit_Wait_1", CurrentPlayer);
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("15.Rin", " * Devouring One", CurrentPlayer, "Anywhere");
      LMove(165, -y, x);
      MoveUnit(16, " Unit. Schnee", CurrentPlayer, "[Skill]Unit_Wait_ALL", "15.Rin");
      MoveLocation("15.Rin", " * Devouring One", CurrentPlayer, "Anywhere");
      LMove(165, y, -x);
      MoveUnit(16, " Unit. Schnee", CurrentPlayer, "[Skill]Unit_Wait_ALL", "15.Rin");
      KillUnitAt(All, " Unit. Schnee", "Anywhere", CurrentPlayer);
      Wait(200);
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
   },
}

radius = 3 / 8 * math.pi;

d = 130;

x = math.sin(radius) * d;
y = math.cos(radius) * d;
x = math.floor(x + 0.5);
y = math.floor(y + 0.5);

Trigger { -- Skill : Combo
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 2000, " * Devouring One");
      Deaths(CurrentPlayer, Exactly, 130, " `SkillStep");
      Bring(CurrentPlayer, AtLeast, 1, " * Devouring One", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 1, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      CreateUnit(25, " Unit. Schnee", "[Skill]Unit_Wait_1", CurrentPlayer);
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("15.Rin", " * Devouring One", CurrentPlayer, "Anywhere");
      LMove(165, x, y);
      MoveUnit(25, " Unit. Schnee", CurrentPlayer, "[Skill]Unit_Wait_ALL", "15.Rin");
      CreateUnit(25, " Unit. Schnee", "[Skill]Unit_Wait_2", CurrentPlayer);
      MoveLocation("15.Rin", " * Devouring One", CurrentPlayer, "Anywhere");
      LMove(165, -x, -y);
      MoveUnit(25, " Unit. Schnee", CurrentPlayer, "[Skill]Unit_Wait_ALL", "15.Rin");
      CreateUnit(25, " Unit. Schnee", "[Skill]Unit_Wait_3", CurrentPlayer);
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("15.Rin", " * Devouring One", CurrentPlayer, "Anywhere");
      LMove(165, -y, x);
      MoveUnit(25, " Unit. Schnee", CurrentPlayer, "[Skill]Unit_Wait_ALL", "15.Rin");
      CreateUnit(25, " Unit. Schnee", "[Skill]Unit_Wait_4", CurrentPlayer);
      MoveLocation("15.Rin", " * Devouring One", CurrentPlayer, "Anywhere");
      LMove(165, y, -x);
      MoveUnit(25, " Unit. Schnee", CurrentPlayer, "[Skill]Unit_Wait_ALL", "15.Rin");
      KillUnitAt(All, " Unit. Schnee", "Anywhere", CurrentPlayer);
      Wait(200);
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
   },
}


radius = 5 / 8 * math.pi;

d = 210;

x = math.sin(radius) * d;
y = math.cos(radius) * d;
x = math.floor(x + 0.5);
y = math.floor(y + 0.5);

Trigger { -- Skill : Combo
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 2000, " * Devouring One");
      Deaths(CurrentPlayer, Exactly, 130, " `SkillStep");
      Bring(CurrentPlayer, AtLeast, 1, " * Devouring One", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 2, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      CreateUnit(36, " Unit. Schnee", "[Skill]Unit_Wait_1", CurrentPlayer);
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("15.Rin", " * Devouring One", CurrentPlayer, "Anywhere");
      LMove(165, x, y);
      MoveUnit(36, " Unit. Schnee", CurrentPlayer, "[Skill]Unit_Wait_ALL", "15.Rin");
      CreateUnit(36, " Unit. Schnee", "[Skill]Unit_Wait_2", CurrentPlayer);
      MoveLocation("15.Rin", " * Devouring One", CurrentPlayer, "Anywhere");
      LMove(165, -x, -y);
      MoveUnit(36, " Unit. Schnee", CurrentPlayer, "[Skill]Unit_Wait_ALL", "15.Rin");
      CreateUnit(36, " Unit. Schnee", "[Skill]Unit_Wait_3", CurrentPlayer);
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("15.Rin", " * Devouring One", CurrentPlayer, "Anywhere");
      LMove(165, -y, x);
      MoveUnit(36, " Unit. Schnee", CurrentPlayer, "[Skill]Unit_Wait_ALL", "15.Rin");
      CreateUnit(36, " Unit. Schnee", "[Skill]Unit_Wait_4", CurrentPlayer);
      MoveLocation("15.Rin", " * Devouring One", CurrentPlayer, "Anywhere");
      LMove(165, y, -x);
      MoveUnit(36, " Unit. Schnee", CurrentPlayer, "[Skill]Unit_Wait_ALL", "15.Rin");
      KillUnitAt(All, " Unit. Schnee", "Anywhere", CurrentPlayer);
      Wait(0);
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
   },
}

Trigger { -- Skill : Combo
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 2000, " * Devouring One");
      Deaths(CurrentPlayer, Exactly, 130, " `SkillStep");
      Bring(CurrentPlayer, AtLeast, 1, " * Devouring One", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 3, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      CreateUnit(4, "100 + 1n Dragoon", "[Skill]Unit_Wait_1", CurrentPlayer);
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("15.Rin", " * Devouring One", CurrentPlayer, "Anywhere");
      LMove(165, x, y);
      MoveUnit(1, "100 + 1n Dragoon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "15.Rin");
      MoveLocation("15.Rin", " * Devouring One", CurrentPlayer, "Anywhere");
      LMove(165, -x, -y);
      MoveUnit(1, "100 + 1n Dragoon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "15.Rin");
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("15.Rin", " * Devouring One", CurrentPlayer, "Anywhere");
      LMove(165, -y, x);
      MoveUnit(1, "100 + 1n Dragoon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "15.Rin");
      MoveLocation("15.Rin", " * Devouring One", CurrentPlayer, "Anywhere");
      LMove(165, y, -x);
      MoveUnit(1, "100 + 1n Dragoon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "15.Rin");
      MoveLocation("15.Rin", " * Devouring One", CurrentPlayer, "Anywhere");
      MoveUnit(All, "100 + 1n Dragoon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "15.Rin");
      Wait(200);
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
   },
}


radius = 7 / 8 * math.pi;

d = 210;

x = math.sin(radius) * d;
y = math.cos(radius) * d;
x = math.floor(x + 0.5);
y = math.floor(y + 0.5);

Trigger { -- Skill : Combo
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 2000, " * Devouring One");
      Deaths(CurrentPlayer, Exactly, 130, " `SkillStep");
      Bring(CurrentPlayer, AtLeast, 1, " * Devouring One", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 4, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      CreateUnit(36, " Unit. Schnee", "[Skill]Unit_Wait_1", CurrentPlayer);
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("15.Rin", " * Devouring One", CurrentPlayer, "Anywhere");
      LMove(165, x, y);
      MoveUnit(36, " Unit. Schnee", CurrentPlayer, "[Skill]Unit_Wait_ALL", "15.Rin");
      CreateUnit(36, " Unit. Schnee", "[Skill]Unit_Wait_2", CurrentPlayer);
      MoveLocation("15.Rin", " * Devouring One", CurrentPlayer, "Anywhere");
      LMove(165, -x, -y);
      MoveUnit(36, " Unit. Schnee", CurrentPlayer, "[Skill]Unit_Wait_ALL", "15.Rin");
      CreateUnit(36, " Unit. Schnee", "[Skill]Unit_Wait_3", CurrentPlayer);
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("15.Rin", " * Devouring One", CurrentPlayer, "Anywhere");
      LMove(165, -y, x);
      MoveUnit(36, " Unit. Schnee", CurrentPlayer, "[Skill]Unit_Wait_ALL", "15.Rin");
      CreateUnit(36, " Unit. Schnee", "[Skill]Unit_Wait_4", CurrentPlayer);
      MoveLocation("15.Rin", " * Devouring One", CurrentPlayer, "Anywhere");
      LMove(165, y, -x);
      MoveUnit(36, " Unit. Schnee", CurrentPlayer, "[Skill]Unit_Wait_ALL", "15.Rin");
      KillUnitAt(All, " Unit. Schnee", "Anywhere", CurrentPlayer);
      Wait(0);
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
   },
}


Trigger { -- Skill : Combo
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 2000, " * Devouring One");
      Deaths(CurrentPlayer, Exactly, 130, " `SkillStep");
      Bring(CurrentPlayer, AtLeast, 1, " * Devouring One", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 5, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      CreateUnit(4, "100 + 1n Dragoon", "[Skill]Unit_Wait_1", CurrentPlayer);
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("15.Rin", " * Devouring One", CurrentPlayer, "Anywhere");
      LMove(165, x, y);
      MoveUnit(1, "100 + 1n Dragoon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "15.Rin");
      MoveLocation("15.Rin", " * Devouring One", CurrentPlayer, "Anywhere");
      LMove(165, -x, -y);
      MoveUnit(1, "100 + 1n Dragoon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "15.Rin");
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("15.Rin", " * Devouring One", CurrentPlayer, "Anywhere");
      LMove(165, -y, x);
      MoveUnit(1, "100 + 1n Dragoon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "15.Rin");
      MoveLocation("15.Rin", " * Devouring One", CurrentPlayer, "Anywhere");
      LMove(165, y, -x);
      MoveUnit(1, "100 + 1n Dragoon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "15.Rin");
      MoveLocation("15.Rin", " * Devouring One", CurrentPlayer, "Anywhere");
      MoveUnit(All, "100 + 1n Dragoon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "15.Rin");
      Wait(200);
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
   },
}


Trigger { -- Skill : Combo
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 2000, " * Devouring One");
      Bring(CurrentPlayer, AtLeast, 1, " * Devouring One", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 130, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 6, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      Wait(3500);
      SetDeaths(CurrentPlayer, SetTo, 0, " `SkillCount");
      SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
      SetDeaths(CurrentPlayer, Add, 12, " `SkillWait");
   },
}