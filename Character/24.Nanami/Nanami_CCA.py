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

            f.EdgeShape(cp, 1, "60 + 1n High Templar", 45, 5, 100);
            KillUnitAt(All, "60 + 1n High Templar", "Anywhere", cp);

            f.SkillWait(cp, 320);

            f.loop[cp] += 1;
         }
         else if (f.loop[cp] == 1)
         {         
            f.EdgeShape(cp, 1, "60 + 1n High Templar", 0, 5, 100);
            KillUnitAt(All, "60 + 1n High Templar", "Anywhere", cp);

            f.SkillWait(cp, 320);

            f.loop[cp] += 1;
         }
         else if (f.loop[cp] == 2)
         {         
            f.EdgeShape(cp, 1, "60 + 1n High Templar", 45, 5, 150);
            KillUnitAt(All, "60 + 1n High Templar", "Anywhere", cp);

            f.SkillWait(cp, 320);

            f.loop[cp] += 1;
         }
         else if (f.loop[cp] == 3)
         {         
            f.EdgeShape(cp, 1, "60 + 1n High Templar", 0, 5, 150);
            KillUnitAt(All, "60 + 1n High Templar", "Anywhere", cp);

            f.SkillWait(cp, 320);

            f.loop[cp] += 1;
         }
         else if (f.loop[cp] == 4)
         {         
            f.Table_Sin(cp, 22, 75);
            f.Table_Cos(cp, 22, 75);

            f.SquareShape(cp, 1, "60 + 1n High Templar", f.CosAngle[cp], f.SinAngle[cp]);
            MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
            MoveUnit(All, "60 + 1n High Templar", cp, "[Skill]Unit_Wait_ALL", f.location[cp]);
            Order("60 + 1n High Templar", cp, "Anywhere", Attack, f.location[cp]);

            f.SkillWait(cp, 160);

            f.loop[cp] += 1;
         }
         else if (f.loop[cp] == 5)
         {         
            f.Table_Sin(cp, 67, 150);
            f.Table_Cos(cp, 67, 150);

            f.SquareShape(cp, 1, "60 + 1n Dragoon", f.CosAngle[cp], f.SinAngle[cp]);
            MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
            MoveUnit(All, "60 + 1n Dragoon", cp, "[Skill]Unit_Wait_ALL", f.location[cp]);
            Order("60 + 1n Dragoon", cp, "Anywhere", Attack, f.location[cp]);

            f.SkillWait(cp, 160);

            f.loop[cp] += 1;
         }
         else if (f.loop[cp] == 6)
         {
            f.EdgeShape(cp, 1, "100 + 1n Dragoon", 45, 5, 150);
            KillUnitAt(All, "100 + 1n Dragoon", "Anywhere", cp);

            f.Table_Sin(cp, 22, 225);
            f.Table_Cos(cp, 22, 225);

            f.SquareShape(cp, 1, "40 + 1n Mojo", f.CosAngle[cp], f.SinAngle[cp]);
            MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
            Order("40 + 1n Mojo", cp, "Anywhere", Attack, f.location[cp]);

            f.SkillWait(cp, 160);

            f.loop[cp] += 1;
         }
         else if (f.loop[cp] == 7)
         {
            f.EdgeShape(cp, 1, "100 + 1n Dragoon", 0, 5, 150);
            KillUnitAt(All, "100 + 1n Dragoon", "Anywhere", cp);

            f.Table_Sin(cp, 22, 275);
            f.Table_Cos(cp, 22, 275);

            f.SquareShape(cp, 1, "60 + 1n Danimoth", f.CosAngle[cp], f.SinAngle[cp]);
            MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
            Order("60 + 1n Danimoth", cp, "Anywhere", Attack, f.location[cp]);

            f.SkillWait(cp, 1120);

            f.loop[cp] += 1;
         }
         else if (f.loop[cp] == 8)
         {
            f.SkillWait(cp, 80);

            f.count[cp] += 1;
            f.loop[cp] = 0;
         }
      }
      else if (f.count[cp] == 1)
      {
         if (f.loop[cp] < 14)
         {       
            KillUnitAt(All, "40 + 1n Wraith", "Anywhere", cp);

            if ((f.loop[cp] / 4) % 2 == 0)
            { 
               f.DotShape(cp, 1, "40 + 1n Wraith", 160 - 40 * (f.loop[cp] % 4) , 40 * (f.loop[cp] % 4));
               f.DotShape(cp, 1, "40 + 1n Wraith", -160 + 40 * (f.loop[cp] % 4), -40 * (f.loop[cp] % 4));
            }
            else if ((f.loop[cp] / 4) % 2 == 1)
            { 
               f.DotShape(cp, 1, "40 + 1n Wraith", -40 * (f.loop[cp] % 4), 160 - 40 * (f.loop[cp] % 4));
               f.DotShape(cp, 1, "40 + 1n Wraith", 40 * (f.loop[cp] % 4), -160 + 40 * (f.loop[cp] % 4));
            }

            MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
            Order("40 + 1n Wraith", cp, "Anywhere", Attack, f.location[cp]);

            f.SkillWait(cp, 320);

            f.loop[cp] += 1;
         }
         else if (f.loop[cp] == 14)
         {
            KillUnitAt(All, "40 + 1n Wraith", "Anywhere", cp);

            f.Voice_Routine(cp, 5);

            f.SkillWait(cp, 80);

            f.count[cp] += 1;
            f.loop[cp] = 0;
         }
      }
      else if (f.count[cp] == 2)
      {
         if (f.loop[cp] < 8)
         {       
            KillUnitAt(All, "40 + 1n Wraith", "Anywhere", cp);

            if ((f.loop[cp] / 4) % 2 == 0)
            { 
               f.DotShape(cp, 1, "40 + 1n Wraith", 160 - 40 * (f.loop[cp] % 4) , 40 * (f.loop[cp] % 4));
               f.DotShape(cp, 1, "40 + 1n Wraith", -160 + 40 * (f.loop[cp] % 4), -40 * (f.loop[cp] % 4));
            }
            else if ((f.loop[cp] / 4) % 2 == 1)
            { 
               f.DotShape(cp, 1, "40 + 1n Wraith", -40 * (f.loop[cp] % 4), 160 - 40 * (f.loop[cp] % 4));
               f.DotShape(cp, 1, "40 + 1n Wraith", 40 * (f.loop[cp] % 4), -160 + 40 * (f.loop[cp] % 4));
            }

            MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
            Order("40 + 1n Wraith", cp, "Anywhere", Attack, f.location[cp]);

            f.SkillWait(cp, 320);

            f.loop[cp] += 1;
         }
         else if (f.loop[cp] == 8)
         {
            KillUnitAt(All, "40 + 1n Wraith", "Anywhere", cp);

            f.SkillWait(cp, 80);

            f.count[cp] += 1;
            f.loop[cp] = 0;
         }
      }

      else if (f.count[cp] == 3)
      {
         KillUnitAt(All, "40 + 1n Mojo", "Anywhere", cp);
         KillUnitAt(All, "60 + 1n Danimoth", "Anywhere", cp);
         KillUnitAt(All, "60 + 1n High Templar", "Anywhere", cp);
         KillUnitAt(All, "60 + 1n Dragoon", "Anywhere", cp);
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
            f.SquareShape(cp, 1, "60 + 1n High Templar", 75, 75);

            KillUnitAt(All, "60 + 1n High Templar", "Anywhere", cp);

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
         if (f.loopC[cp] == 8) f.loopC[cp] = 0;
         if (f.loopC[cp] < 4)
         {
            f.DotShape(cp, 1, " Unit. Hoffnung 25000", 160 - 40 * f.loopC[cp], 40 * f.loopC[cp]);
            f.DotShape(cp, 1, " Unit. Hoffnung 25000", -160 + 40 * f.loopC[cp], -40 * f.loopC[cp]);
            f.DotShape(cp, 1, "100 + 1n Dragoon", -40 * f.loopC[cp], 160 - 40 * f.loopC[cp]);
            f.DotShape(cp, 1, "100 + 1n Dragoon", 40 * f.loopC[cp], -160 + 40 * f.loopC[cp]);

            KillUnitAt(All, " Unit. Hoffnung 25000", "Anywhere", cp);
            KillUnitAt(All, "100 + 1n Dragoon", "Anywhere", cp);

            f.SkillWaitC(cp, 320);

            f.loopC[cp] += 1;
         }
         else if (f.loopC[cp] < 8)
         {
            f.DotShape(cp, 1, " Unit. Hoffnung 25000", -40 * (f.loopC[cp] - 4), 160 - 40 * (f.loopC[cp] - 4));
            f.DotShape(cp, 1, " Unit. Hoffnung 25000", 40 * (f.loopC[cp] - 4), -160 + 40 * (f.loopC[cp] - 4));
            f.DotShape(cp, 1, "100 + 1n Dragoon", 160 - 40 * (f.loopC[cp] - 4), 40 * (f.loopC[cp] - 4));
            f.DotShape(cp, 1, "100 + 1n Dragoon", -160 + 40 * (f.loopC[cp] - 4), -40 * (f.loopC[cp] - 4));

            KillUnitAt(All, " Unit. Hoffnung 25000", "Anywhere", cp);
            KillUnitAt(All, "100 + 1n Dragoon", "Anywhere", cp);

            f.SkillWaitC(cp, 320);

            f.loopC[cp] += 1;
         }
      }


   }
}