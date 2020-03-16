radius1 = 1 / 4 * math.pi;
radius2 = math.pi;

for i = 0, 7, 1 do

d = 50 + i * 10;

x1 = math.sin(radius1) * d;
y1 = math.cos(radius1) * d;
x1 = math.floor(x1 + 0.5);
y1 = math.floor(y1 + 0.5);

x2 = math.sin(radius2) * d;
y2 = math.cos(radius2) * d;
x2 = math.floor(x2 + 0.5);
y2 = math.floor(y2 + 0.5);

Trigger { -- Skill : Combo
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 2000, " * Devouring One");
      Deaths(CurrentPlayer, Exactly, 110, " `SkillStep");
      Bring(CurrentPlayer, AtLeast, 1, " * Devouring One", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, i, " `SkillLoop");
      Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      CreateUnit(8, "60 + 1n High Templar", "[Skill]Unit_Wait_1", CurrentPlayer);
      CreateUnit(8, "40 + 1n Gantrithor", "[Skill]Unit_Wait_2", CurrentPlayer);
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("15.Rin", " * Devouring One", CurrentPlayer, "Anywhere");
      LMove(165, x1, y1);
      MoveUnit(1, "60 + 1n High Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "15.Rin");
      MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "15.Rin");
      MoveLocation("15.Rin", " * Devouring One", CurrentPlayer, "Anywhere");
      LMove(165, -x1, -y1);
      MoveUnit(1, "60 + 1n High Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "15.Rin");
      MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "15.Rin");
      MoveLocation("15.Rin", " * Devouring One", CurrentPlayer, "Anywhere");
      LMove(165, y1, -x1);
      MoveUnit(1, "60 + 1n High Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "15.Rin");
      MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "15.Rin");
      MoveLocation("15.Rin", " * Devouring One", CurrentPlayer, "Anywhere");
      LMove(165, -y1, x1);
      MoveUnit(1, "60 + 1n High Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "15.Rin");
      MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "15.Rin");
      MoveLocation("15.Rin", " * Devouring One", CurrentPlayer, "Anywhere");
      LMove(165, x2, y2);
      MoveUnit(1, "60 + 1n High Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "15.Rin");
      MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "15.Rin");
      MoveLocation("15.Rin", " * Devouring One", CurrentPlayer, "Anywhere");
      LMove(165, -x2, -y2);
      MoveUnit(1, "60 + 1n High Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "15.Rin");
      MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "15.Rin");
      MoveLocation("15.Rin", " * Devouring One", CurrentPlayer, "Anywhere");
      LMove(165, y2, -x2);
      MoveUnit(1, "60 + 1n High Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "15.Rin");
      MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "15.Rin");
      MoveLocation("15.Rin", " * Devouring One", CurrentPlayer, "Anywhere");
      LMove(165, -y2, x2);
      MoveUnit(1, "60 + 1n High Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "15.Rin");
      MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "15.Rin");
      KillUnitAt(All, "40 + 1n Gantrithor", "Anywhere", CurrentPlayer);
      KillUnitAt(All, "60 + 1n High Templar", "Anywhere", CurrentPlayer);
      Wait(0);
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
   },
}
end

Trigger { -- Skill : Combo
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 2000, " * Devouring One");
      Deaths(CurrentPlayer, Exactly, 110, " `SkillStep");
      Bring(CurrentPlayer, AtLeast, 1, " * Devouring One", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 8, " `SkillLoop");
      Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      CreateUnit(8, "60 + 1n Dragoon", "[Skill]Unit_Wait_1", CurrentPlayer);
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("15.Rin", " * Devouring One", CurrentPlayer, "Anywhere");
      LMove(165, x1, y1);
      MoveUnit(1, "60 + 1n Dragoon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "15.Rin");
      MoveLocation("15.Rin", " * Devouring One", CurrentPlayer, "Anywhere");
      LMove(165, -x1, -y1);
      MoveUnit(1, "60 + 1n Dragoon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "15.Rin");
      MoveLocation("15.Rin", " * Devouring One", CurrentPlayer, "Anywhere");
      LMove(165, y1, -x1);
      MoveUnit(1, "60 + 1n Dragoon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "15.Rin");
      MoveLocation("15.Rin", " * Devouring One", CurrentPlayer, "Anywhere");
      LMove(165, -y1, x1);
      MoveUnit(1, "60 + 1n Dragoon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "15.Rin");
      MoveLocation("15.Rin", " * Devouring One", CurrentPlayer, "Anywhere");
      LMove(165, x2, y2);
      MoveUnit(1, "60 + 1n Dragoon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "15.Rin");
      MoveLocation("15.Rin", " * Devouring One", CurrentPlayer, "Anywhere");
      LMove(165, -x2, -y2);
      MoveUnit(1, "60 + 1n Dragoon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "15.Rin");
      MoveLocation("15.Rin", " * Devouring One", CurrentPlayer, "Anywhere");
      LMove(165, y2, -x2);
      MoveUnit(1, "60 + 1n Dragoon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "15.Rin");
      MoveLocation("15.Rin", " * Devouring One", CurrentPlayer, "Anywhere");
      LMove(165, -y2, x2);
      MoveUnit(1, "60 + 1n Dragoon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "15.Rin");
      MoveLocation("15.Rin", " * Devouring One", CurrentPlayer, "Anywhere");
      MoveUnit(All, "60 + 1n Dragoon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "15.Rin");
      Wait(1000);
      SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
      SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
   },
}

for i = 0, 3, 1 do

d = 130 - i * 20;

x1 = math.sin(radius1) * d;
y1 = math.cos(radius1) * d;
x1 = math.floor(x1 + 0.5);
y1 = math.floor(y1 + 0.5);

x2 = math.sin(radius2) * d;
y2 = math.cos(radius2) * d;
x2 = math.floor(x2 + 0.5);
y2 = math.floor(y2 + 0.5);

Trigger { -- Skill : Combo
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 2000, " * Devouring One");
      Deaths(CurrentPlayer, Exactly, 110, " `SkillStep");
      Bring(CurrentPlayer, AtLeast, 1, " * Devouring One", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 2, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, i, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      CreateUnit(32, " Unit. Schnee", "[Skill]Unit_Wait_1", CurrentPlayer);
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("15.Rin", " * Devouring One", CurrentPlayer, "Anywhere");
      LMove(165, x1, y1);
      MoveUnit(4, " Unit. Schnee", CurrentPlayer, "[Skill]Unit_Wait_ALL", "15.Rin");
      MoveLocation("15.Rin", " * Devouring One", CurrentPlayer, "Anywhere");
      LMove(165, -x1, -y1);
      MoveUnit(4, " Unit. Schnee", CurrentPlayer, "[Skill]Unit_Wait_ALL", "15.Rin");
      MoveLocation("15.Rin", " * Devouring One", CurrentPlayer, "Anywhere");
      LMove(165, y1, -x1);
      MoveUnit(4, " Unit. Schnee", CurrentPlayer, "[Skill]Unit_Wait_ALL", "15.Rin");
      MoveLocation("15.Rin", " * Devouring One", CurrentPlayer, "Anywhere");
      LMove(165, -y1, x1);
      MoveUnit(4, " Unit. Schnee", CurrentPlayer, "[Skill]Unit_Wait_ALL", "15.Rin");
      MoveLocation("15.Rin", " * Devouring One", CurrentPlayer, "Anywhere");
      LMove(165, x2, y2);
      MoveUnit(4, " Unit. Schnee", CurrentPlayer, "[Skill]Unit_Wait_ALL", "15.Rin");
      MoveLocation("15.Rin", " * Devouring One", CurrentPlayer, "Anywhere");
      LMove(165, -x2, -y2);
      MoveUnit(4, " Unit. Schnee", CurrentPlayer, "[Skill]Unit_Wait_ALL", "15.Rin");
      MoveLocation("15.Rin", " * Devouring One", CurrentPlayer, "Anywhere");
      LMove(165, y2, -x2);
      MoveUnit(4, " Unit. Schnee", CurrentPlayer, "[Skill]Unit_Wait_ALL", "15.Rin");
      MoveLocation("15.Rin", " * Devouring One", CurrentPlayer, "Anywhere");
      LMove(165, -y2, x2);
      MoveUnit(4, " Unit. Schnee", CurrentPlayer, "[Skill]Unit_Wait_ALL", "15.Rin");
      KillUnitAt(All, " Unit. Schnee", "Anywhere", CurrentPlayer);
      Wait(0);
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
   },
}
end

d = 130 - 4 * 20;

x1 = math.sin(radius1) * d;
y1 = math.cos(radius1) * d;
x1 = math.floor(x1 + 0.5);
y1 = math.floor(y1 + 0.5);

x2 = math.sin(radius2) * d;
y2 = math.cos(radius2) * d;
x2 = math.floor(x2 + 0.5);
y2 = math.floor(y2 + 0.5);

Trigger { -- Skill : Combo
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 2000, " * Devouring One");
      Deaths(CurrentPlayer, Exactly, 110, " `SkillStep");
      Bring(CurrentPlayer, AtLeast, 1, " * Devouring One", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 2, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 4, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      CreateUnit(8, "60 + 1n High Templar", "[Skill]Unit_Wait_1", CurrentPlayer);
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("15.Rin", " * Devouring One", CurrentPlayer, "Anywhere");
      LMove(165, x1, y1);
      MoveUnit(1, "60 + 1n High Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "15.Rin");
      MoveLocation("15.Rin", " * Devouring One", CurrentPlayer, "Anywhere");
      LMove(165, -x1, -y1);
      MoveUnit(1, "60 + 1n High Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "15.Rin");
      MoveLocation("15.Rin", " * Devouring One", CurrentPlayer, "Anywhere");
      LMove(165, y1, -x1);
      MoveUnit(1, "60 + 1n High Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "15.Rin");
      MoveLocation("15.Rin", " * Devouring One", CurrentPlayer, "Anywhere");
      LMove(165, -y1, x1);
      MoveUnit(1, "60 + 1n High Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "15.Rin");
      MoveLocation("15.Rin", " * Devouring One", CurrentPlayer, "Anywhere");
      LMove(165, x2, y2);
      MoveUnit(1, "60 + 1n High Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "15.Rin");
      MoveLocation("15.Rin", " * Devouring One", CurrentPlayer, "Anywhere");
      LMove(165, -x2, -y2);
      MoveUnit(1, "60 + 1n High Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "15.Rin");
      MoveLocation("15.Rin", " * Devouring One", CurrentPlayer, "Anywhere");
      LMove(165, y2, -x2);
      MoveUnit(1, "60 + 1n High Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "15.Rin");
      MoveLocation("15.Rin", " * Devouring One", CurrentPlayer, "Anywhere");
      LMove(165, -y2, x2);
      MoveUnit(1, "60 + 1n High Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "15.Rin");
      MoveLocation("15.Rin", " * Devouring One", CurrentPlayer, "Anywhere");
      MoveUnit(All, "60 + 1n High Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "15.Rin");
      Order("60 + 1n High Templar", CurrentPlayer, "Anywhere", Attack, "15.Rin");
      Wait(300);
      SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
      SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
   },
}

for i = 0, 3, 1 do

d = 130 - i * 20;

x1 = math.sin(radius1) * d;
y1 = math.cos(radius1) * d;
x1 = math.floor(x1 + 0.5);
y1 = math.floor(y1 + 0.5);

x2 = math.sin(radius2) * d;
y2 = math.cos(radius2) * d;
x2 = math.floor(x2 + 0.5);
y2 = math.floor(y2 + 0.5);

Trigger { -- Skill : Combo
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 2000, " * Devouring One");
      Deaths(CurrentPlayer, Exactly, 110, " `SkillStep");
      Bring(CurrentPlayer, AtLeast, 1, " * Devouring One", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 3, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, i, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      CreateUnit(32, " Unit. Schnee", "[Skill]Unit_Wait_1", CurrentPlayer);
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("15.Rin", " * Devouring One", CurrentPlayer, "Anywhere");
      LMove(165, x1, y1);
      MoveUnit(4, " Unit. Schnee", CurrentPlayer, "[Skill]Unit_Wait_ALL", "15.Rin");
      MoveLocation("15.Rin", " * Devouring One", CurrentPlayer, "Anywhere");
      LMove(165, -x1, -y1);
      MoveUnit(4, " Unit. Schnee", CurrentPlayer, "[Skill]Unit_Wait_ALL", "15.Rin");
      MoveLocation("15.Rin", " * Devouring One", CurrentPlayer, "Anywhere");
      LMove(165, y1, -x1);
      MoveUnit(4, " Unit. Schnee", CurrentPlayer, "[Skill]Unit_Wait_ALL", "15.Rin");
      MoveLocation("15.Rin", " * Devouring One", CurrentPlayer, "Anywhere");
      LMove(165, -y1, x1);
      MoveUnit(4, " Unit. Schnee", CurrentPlayer, "[Skill]Unit_Wait_ALL", "15.Rin");
      MoveLocation("15.Rin", " * Devouring One", CurrentPlayer, "Anywhere");
      LMove(165, x2, y2);
      MoveUnit(4, " Unit. Schnee", CurrentPlayer, "[Skill]Unit_Wait_ALL", "15.Rin");
      MoveLocation("15.Rin", " * Devouring One", CurrentPlayer, "Anywhere");
      LMove(165, -x2, -y2);
      MoveUnit(4, " Unit. Schnee", CurrentPlayer, "[Skill]Unit_Wait_ALL", "15.Rin");
      MoveLocation("15.Rin", " * Devouring One", CurrentPlayer, "Anywhere");
      LMove(165, y2, -x2);
      MoveUnit(4, " Unit. Schnee", CurrentPlayer, "[Skill]Unit_Wait_ALL", "15.Rin");
      MoveLocation("15.Rin", " * Devouring One", CurrentPlayer, "Anywhere");
      LMove(165, -y2, x2);
      MoveUnit(4, " Unit. Schnee", CurrentPlayer, "[Skill]Unit_Wait_ALL", "15.Rin");
      KillUnitAt(All, " Unit. Schnee", "Anywhere", CurrentPlayer);
      Wait(0);
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
   },
}
end

Trigger { -- Skill : Combo
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 2000, " * Devouring One");
      Deaths(CurrentPlayer, Exactly, 110, " `SkillStep");
      Bring(CurrentPlayer, AtLeast, 1, " * Devouring One", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 3, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 4, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      Wait(0);
      KillUnitAt(All, "60 + 1n High Templar", "Anywhere", CurrentPlayer);
      SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
      SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
   },
}

Trigger { -- Skill : Combo
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 2000, " * Devouring One");
      Bring(CurrentPlayer, AtLeast, 1, " * Devouring One", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 110, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 4, " `SkillCount");
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