import Function as f;

function main(cp)
{
   f.HoldPosition(cp);
   f.BanReturn(cp);
   MoveLocation("24.Nanami_Bozo", f.heroID[cp], cp, "Anywhere");
   
   if (f.delay[cp] == 0)
   {
      if (f.count[cp] == 0)
      {
         if (f.loop[cp] == 0)
         {         
            if (cp < 3) SetSwitch("Passive - Nanami1", Set);
            else SetSwitch("Passive - Nanami2", Set);

            f.DotShape(cp, 1, "60 + 1n Archon", -100, 100);
            f.DotShape(cp, 1, "60 + 1n Siege", -100, 100);
            KillUnitAt(All, "60 + 1n Archon", "Anywhere", cp);

            f.SkillWait(cp, 160);

            f.loop[cp] += 1;
         }
         else if (f.loop[cp] == 1)
         {         
            f.DotShape(cp, 1, "60 + 1n Archon", 100, -100);
            f.DotShape(cp, 1, "60 + 1n Siege", 100, -100);
            KillUnitAt(All, "60 + 1n Archon", "Anywhere", cp);

            f.SkillWait(cp, 160);

            f.loop[cp] += 1;
         }
         else if (f.loop[cp] == 2)
         {         
            f.DotShape(cp, 1, "60 + 1n Archon", 100, 100);
            f.DotShape(cp, 1, "60 + 1n Siege", 100, 100);
            KillUnitAt(All, "60 + 1n Archon", "Anywhere", cp);

            f.SkillWait(cp, 160);

            f.loop[cp] += 1;
         }
         else if (f.loop[cp] == 3)
         {         
            f.DotShape(cp, 1, "60 + 1n Archon", -100, -100);
            f.DotShape(cp, 1, "60 + 1n Siege", -100, -100);
            KillUnitAt(All, "60 + 1n Archon", "Anywhere", cp);

            f.SkillWait(cp, 160);

            f.loop[cp] += 1;
         }
         else if (f.loop[cp] == 4)
         {         
            f.DotShape(cp, 1, " Unit. Hoffnung 25000", -200, 0);
            f.DotShape(cp, 1, "60 + 1n Siege", -200, 0);
            KillUnitAt(All, " Unit. Hoffnung 25000", "Anywhere", cp);

            f.SkillWait(cp, 160);

            f.loop[cp] += 1;
         }
         else if (f.loop[cp] == 5)
         {         
            f.DotShape(cp, 1, " Unit. Hoffnung 25000", 200, 0);
            f.DotShape(cp, 1, "60 + 1n Siege", 200, 0);
            KillUnitAt(All, " Unit. Hoffnung 25000", "Anywhere", cp);

            f.SkillWait(cp, 160);

            f.loop[cp] += 1;
         }
         else if (f.loop[cp] == 6)
         {
            f.DotShape(cp, 1, " Unit. Hoffnung 25000", 0, 200);
            f.DotShape(cp, 1, "60 + 1n Siege", 0, 200);
            KillUnitAt(All, " Unit. Hoffnung 25000", "Anywhere", cp);

            f.SkillWait(cp, 160);

            f.loop[cp] += 1;
         }
         else if (f.loop[cp] == 7)
         {
            f.DotShape(cp, 1, " Unit. Hoffnung 25000", 0, -200);
            f.DotShape(cp, 1, "60 + 1n Siege", 0, -200);
            KillUnitAt(All, " Unit. Hoffnung 25000", "Anywhere", cp);

            f.SkillWait(cp, 160);

            f.loop[cp] += 1;
         }
         else if (f.loop[cp] == 8)
         {
            f.EdgeShape(cp, 1, " Unit. Hoffnung 25000", 0, 7, 150);
            KillUnitAt(All, " Unit. Hoffnung 25000", "Anywhere", cp);

            f.SkillWait(cp, 160);

            f.loop[cp] += 1;
         }
         else if (f.loop[cp] == 9)
         {
            f.EdgeShape(cp, 1, " Unit. Hoffnung 25000", 45, 7, 150);
            KillUnitAt(All, " Unit. Hoffnung 25000", "Anywhere", cp);
            f.EdgeShape(cp, 1, "60 + 1n Danimoth", 0, 3, 150);

            MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
            Order("60 + 1n Danimoth", cp, "Anywhere", Attack, f.location[cp]);

            f.SkillWait(cp, 1840);

            f.loop[cp] += 1;
         }
         else if (f.loop[cp] == 10)
         {
            f.SkillWait(cp, 80);

            f.count[cp] += 1;
            f.loop[cp] = 0;
         }
      }
      else if (f.count[cp] == 1)
      {
         if (f.loop[cp] == 0)
         {         
            f.EdgeShape(cp, 1, "60 + 1n High Templar", 45, 5, 100);
            KillUnitAt(All, "60 + 1n High Templar", "Anywhere", cp);

            f.SkillWait(cp, 160);

            f.loop[cp] += 1;
         }
         else if (f.loop[cp] == 1)
         {         
            f.EdgeShape(cp, 1, "60 + 1n High Templar", 0, 5, 100);
            KillUnitAt(All, "60 + 1n High Templar", "Anywhere", cp);

            f.SkillWait(cp, 160);

            f.loop[cp] += 1;
         }
         else if (f.loop[cp] == 2)
         {         
            f.EdgeShape(cp, 1, "60 + 1n High Templar", 45, 5, 150);
            KillUnitAt(All, "60 + 1n High Templar", "Anywhere", cp);

            f.SkillWait(cp, 160);

            f.loop[cp] += 1;
         }
         else if (f.loop[cp] == 3)
         {         
            f.EdgeShape(cp, 1, "60 + 1n High Templar", 0, 5, 150);
            KillUnitAt(All, "60 + 1n High Templar", "Anywhere", cp);

            f.SkillWait(cp, 160);

            f.loop[cp] += 1;
         }
         else if (f.loop[cp] == 4)
         {
            f.EdgeShape(cp, 1, "100 + 1n Dragoon", 45, 5, 150);
            KillUnitAt(All, "100 + 1n Dragoon", "Anywhere", cp);

            f.EdgeShape(cp, 1, "40 + 1n Mojo", 45, 3, 150);
            MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
            Order("40 + 1n Mojo", cp, "Anywhere", Attack, f.location[cp]);

            f.SkillWait(cp, 160);

            f.loop[cp] += 1;
         }
         else if (f.loop[cp] == 5)
         {
            f.EdgeShape(cp, 1, "100 + 1n Dragoon", 0, 5, 150);
            KillUnitAt(All, "100 + 1n Dragoon", "Anywhere", cp);

            f.SkillWait(cp, 1120);

            f.loop[cp] += 1;
         }
         else if (f.loop[cp] == 6)
         {
            f.SkillWait(cp, 80);

            f.Voice_Routine(cp, 7);

            f.count[cp] += 1;
            f.loop[cp] = 0;
            f.loopC[cp] = 0;
         }

      }
      else if (f.count[cp] == 2)
      {
         if (f.loop[cp] == 0)
         {
            f.EdgeShape(cp, 1, "60 + 1n High Templar", 45, 3, 100);
            MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
            MoveUnit(All, "60 + 1n High Templar", cp, "[Skill]Unit_Wait_ALL", f.location[cp]);
            Order("60 + 1n High Templar", cp, "Anywhere", Attack, f.location[cp]);

            f.SkillWait(cp, 3120);

            f.loop[cp] += 1;
         }
         else if (f.loop[cp] == 1)
         {
            f.SkillWait(cp, 80);

            f.count[cp] += 1;
            f.loop[cp] = 0;
         }

      }

      else if (f.count[cp] == 3)
      {
         KillUnitAt(All, "60 + 1n Danimoth", "Anywhere", cp);
         KillUnitAt(All, "60 + 1n Siege", "Anywhere", cp);
         KillUnitAt(All, "40 + 1n Mojo", "Anywhere", cp);
         KillUnitAt(All, "60 + 1n High Templar", "Anywhere", cp);
         SetSwitch("Passive - Nanami1", Clear);
         SetSwitch("Passive - Nanami2", Clear);

         f.SkillEnd(cp);
      }
   }
   if (f.delayB[cp] == 0)
   {
      if (f.count[cp] < 3)
      {
         if (f.loopB[cp] == 0)
         {
            f.SquareShape(cp, 1, " Unit. Schnee", 75, 75);

            KillUnitAt(All, " Unit. Schnee", "Anywhere", cp);

            f.SkillWaitB(cp, 160);

            f.loopB[cp] += 1;
         }
         else if (f.loopB[cp] == 1)
         {
            f.SquareShape(cp, 1, "60 + 1n Archon", 150, 0);

            KillUnitAt(All, "60 + 1n Archon", "Anywhere", cp);

            f.SkillWaitB(cp, 160);

            f.loopB[cp] += 1;
         }
         else if (f.loopB[cp] == 2)
         {
            f.SquareShape(cp, 1, "Protoss Dark Archon", 150, 75);

            KillUnitAt(All, "Protoss Dark Archon", "Anywhere", cp);

            f.SkillWaitB(cp, 160);

            f.loopB[cp] += 1;
         }
         else if (f.loopB[cp] == 3)
         {
            f.SquareShape(cp, 1, "60 + 1n Archon", 150, 150);

            KillUnitAt(All, "60 + 1n Archon", "Anywhere", cp);

            f.SkillWaitB(cp, 160);

            f.loopB[cp] += 1;
         }
         else if (f.loopB[cp] == 4)
         {
            f.SquareShape(cp, 1, "Protoss Dark Archon", 75, 150);

            KillUnitAt(All, "Protoss Dark Archon", "Anywhere", cp);

            f.SkillWaitB(cp, 160);

            f.loopB[cp] = 0;
         }
      }
   }
   if (f.delayC[cp] == 0)
   {
      if (f.count[cp] < 2 && f.count[cp] > 0)
      {
         if (f.loopC[cp] == 8) f.loopC[cp] = 0;
         if (f.loopC[cp] < 4)
         {
            f.DotShape(cp, 1, " Unit. Schnee", 160 - 40 * f.loopC[cp], 40 * f.loopC[cp]);
            f.DotShape(cp, 1, " Unit. Schnee", -160 + 40 * f.loopC[cp], -40 * f.loopC[cp]);
            f.DotShape(cp, 1, "40 + 1n Zealot", -40 * f.loopC[cp], 160 - 40 * f.loopC[cp]);
            f.DotShape(cp, 1, "40 + 1n Zealot", 40 * f.loopC[cp], -160 + 40 * f.loopC[cp]);

            KillUnitAt(All, " Unit. Schnee", "Anywhere", cp);
            KillUnitAt(All, "40 + 1n Zealot", "Anywhere", cp);

            f.SkillWaitC(cp, 320);

            f.loopC[cp] += 1;
         }
         else if (f.loopC[cp] < 8)
         {
            f.DotShape(cp, 1, " Unit. Schnee", -40 * (f.loopC[cp] - 4), 160 - 40 * (f.loopC[cp] - 4));
            f.DotShape(cp, 1, " Unit. Schnee", 40 * (f.loopC[cp] - 4), -160 + 40 * (f.loopC[cp] - 4));
            f.DotShape(cp, 1, "40 + 1n Zealot", 160 - 40 * (f.loopC[cp] - 4), 40 * (f.loopC[cp] - 4));
            f.DotShape(cp, 1, "40 + 1n Zealot", -160 + 40 * (f.loopC[cp] - 4), -40 * (f.loopC[cp] - 4));

            KillUnitAt(All, " Unit. Schnee", "Anywhere", cp);
            KillUnitAt(All, "40 + 1n Zealot", "Anywhere", cp);

            f.SkillWaitC(cp, 320);

            f.loopC[cp] += 1;
         }
      }
      else if (f.count[cp] < 3 && f.count[cp] > 1)
      {
         if (f.loopC[cp] == 2) f.loopC[cp] = 0;
         if (f.loopC[cp] < 2)
         {
            f.Table_Sin(cp, 22 + 45 * f.loopC[cp], 100 + 50 * f.loopC[cp]);
            f.Table_Cos(cp, 22 + 45 * f.loopC[cp], 100 + 50 * f.loopC[cp]);

            f.NxNSquareShapeAt(cp, 1, " Unit. Schnee", 3, 32, f.CosAngle[cp], f.SinAngle[cp]);
            f.NxNSquareShapeAt(cp, 1, " Unit. Schnee", 3, 32, -f.CosAngle[cp], -f.SinAngle[cp]);
            f.NxNSquareShapeAt(cp, 1, " Unit. Schnee", 3, 32, -f.SinAngle[cp], f.CosAngle[cp]);
            f.NxNSquareShapeAt(cp, 1, " Unit. Schnee", 3, 32, f.SinAngle[cp], -f.CosAngle[cp]);

            KillUnitAt(All, " Unit. Schnee", "Anywhere", cp);

            f.SkillWaitC(cp, 320);

            f.loopC[cp] += 1;
         }
      }


   }
}