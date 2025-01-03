import Function as f;

function main(cp)
{
   f.HoldPosition(cp);
   f.BanReturn(cp);
   
   if (f.delay[cp] == 0)
   {
      if (f.count[cp] == 0)
      {
         if (f.loop[cp] == 0)
         {
            f.EdgeShape(cp, 1, "60 + 1n Archon", 0, 5, 100);
            KillUnitAt(All, "60 + 1n Archon", "Anywhere", cp);
            f.LineShape(cp, 1, "Kakaru (Twilight)", 45, 5, 50, 100);
            f.LineShape(cp, 1, "Kakaru (Twilight)", 225, 5, 50, 100);
            KillUnitAt(All, "Kakaru (Twilight)", "Anywhere", cp);

            f.SkillWait(cp, 80);

            f.loop[cp] += 1;
         }
         else if (f.loop[cp] == 1)
         {
            f.LineShape(cp, 1, "40 + 1n Guardian", 135, 5, 50, 100);
            f.LineShape(cp, 1, "40 + 1n Guardian", 315, 5, 50, 100);
            KillUnitAt(All, "40 + 1n Guardian", "Anywhere", cp);

            f.LineShape(cp, 1, "40 + 1n Marine", 135, 5, 50, 100);
            f.LineShape(cp, 1, "40 + 1n Marine", 315, 5, 50, 100);

            MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
            MoveUnit(All, "40 + 1n Marine", cp, "[Skill]Unit_Wait_ALL", f.location[cp]);
            Order("40 + 1n Marine", cp, "Anywhere", Attack, f.location[cp]);

            f.SkillWait(cp, 240);

            f.loop[cp] += 1;
         }
         else if (f.loop[cp] == 2)
         {
            KillUnitAt(All, "40 + 1n Marine", "Anywhere", cp);

            f.EdgeShape(cp, 1, "60 + 1n Archon", 0, 5, 100);
            KillUnitAt(All, "60 + 1n Archon", "Anywhere", cp);
            f.LineShape(cp, 1, "Kakaru (Twilight)", 135, 5, 50, 100);
            f.LineShape(cp, 1, "Kakaru (Twilight)", 315, 5, 50, 100);
            KillUnitAt(All, "Kakaru (Twilight)", "Anywhere", cp);

            f.SkillWait(cp, 80);

            f.loop[cp] += 1;
         }
         else if (f.loop[cp] == 3)
         {
            f.LineShape(cp, 1, "40 + 1n Guardian", 45, 5, 50, 100);
            f.LineShape(cp, 1, "40 + 1n Guardian", 225, 5, 50, 100);
            KillUnitAt(All, "40 + 1n Guardian", "Anywhere", cp);

            f.LineShape(cp, 1, "40 + 1n Marine", 45, 5, 50, 100);
            f.LineShape(cp, 1, "40 + 1n Marine", 225, 5, 50, 100);

            MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
            MoveUnit(All, "40 + 1n Marine", cp, "[Skill]Unit_Wait_ALL", f.location[cp]);
            Order("40 + 1n Marine", cp, "Anywhere", Attack, f.location[cp]);

            f.SkillWait(cp, 240);

            f.loop[cp] += 1;
         }
         else if (f.loop[cp] == 4)
         {
            KillUnitAt(All, "40 + 1n Marine", "Anywhere", cp);

            f.SkillWait(cp, 880);

            f.loop[cp] += 1;
         }
         else if (f.loop[cp] == 5)
         {
            f.SkillWait(cp, 80);

            f.count[cp] += 1;
            f.loop[cp] = 0;
         }
      }
      else if (f.count[cp] == 1)
      {
         if (f.loop[cp] < 4)
         {         
            f.DotShape(cp, 1, "40 + 1n Wraith", 160 - 40 * f.loop[cp], 40 * f.loop[cp]);
            f.DotShape(cp, 1, "40 + 1n Wraith", -160 + 40 * f.loop[cp], -40 * f.loop[cp]);
            if (f.loop[cp] % 2 == 0)
            {
               f.DotShape(cp, 1, "40 + 1n Goliath", 160 - 40 * f.loop[cp], 40 * f.loop[cp]);
               f.DotShape(cp, 1, "40 + 1n Goliath", -160 + 40 * f.loop[cp], -40 * f.loop[cp]);
            }

            KillUnitAt(All, "40 + 1n Wraith", "Anywhere", cp);

            MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
            MoveUnit(All, "40 + 1n Goliath", cp, "[Skill]Unit_Wait_ALL", f.location[cp]);
            Order("40 + 1n Goliath", cp, "Anywhere", Attack, f.location[cp]);

            f.SkillWait(cp, 80);
            f.loop[cp] += 1;
         }
         else if (f.loop[cp] < 8)
         {
            f.DotShape(cp, 1, "40 + 1n Wraith", -40 * (f.loop[cp] - 4), 160 - 40 * (f.loop[cp] - 4));
            f.DotShape(cp, 1, "40 + 1n Wraith", 40 * (f.loop[cp] - 4), -160 + 40 * (f.loop[cp] - 4));

            if (f.loop[cp] % 2 == 0)
            {
               f.DotShape(cp, 1, "40 + 1n Goliath", -40 * (f.loop[cp] - 4), 160 - 40 * (f.loop[cp] - 4));
               f.DotShape(cp, 1, "40 + 1n Goliath", 40 * (f.loop[cp] - 4), -160 + 40 * (f.loop[cp] - 4));
            }

            KillUnitAt(All, "40 + 1n Wraith", "Anywhere", cp);

            MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
            MoveUnit(All, "40 + 1n Goliath", cp, "[Skill]Unit_Wait_ALL", f.location[cp]);
            Order("40 + 1n Goliath", cp, "Anywhere", Attack, f.location[cp]);

            f.SkillWait(cp, 80);

            f.loop[cp] += 1;
         }
         else if (f.loop[cp] < 12)
         {
            RemoveUnitAt(All, "40 + 1n Mojo", "Anywhere", cp);

            f.Table_Sin(cp, f.loop[cp] * 45, 75);
            f.Table_Cos(cp, f.loop[cp] * 45, 75);

            f.SquareShape(cp, 1, "40 + 1n Mojo", f.CosAngle[cp], f.SinAngle[cp]);
            f.SquareShape(cp, 1, "60 + 1n Archon", f.CosAngle[cp], f.SinAngle[cp]);
            KillUnitAt(All, "60 + 1n Archon", "Anywhere", cp);

            f.Table_Sin(cp, f.loop[cp] * 45 + 45, 75);
            f.Table_Cos(cp, f.loop[cp] * 45 + 45, 75);

            f.SquareShape(cp, 1, "Kakaru (Twilight)", f.CosAngle[cp], f.SinAngle[cp]);
            f.SquareShape(cp, 1, "40 + 1n Zealot", f.CosAngle[cp], f.SinAngle[cp]);
            KillUnitAt(All, "Kakaru (Twilight)", "Anywhere", cp);
            KillUnitAt(All, "40 + 1n Zealot", "Anywhere", cp);

            MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
            Order("40 + 1n Mojo", cp, "Anywhere", Attack, f.location[cp]);

            f.SkillWait(cp, 160);

            f.loop[cp] += 1;
         }
         else if (f.loop[cp] == 12)
         {         
            RemoveUnitAt(All, "40 + 1n Mojo", "Anywhere", cp);

            f.SkillWait(cp, 480);

            f.count[cp] += 1;
            f.loop[cp] = 0;
         }
      }
      else if (f.count[cp] == 2)
      {
         if (f.loop[cp] == 0)
         {         
            f.EdgeShape(cp, 1, "40 + 1n Guardian", 0, 5, 100);
            f.EdgeShape(cp, 1, "Protoss Dark Archon", 0, 5, 100);
            KillUnitAt(All, "40 + 1n Guardian", "Anywhere", cp);
            KillUnitAt(All, "Protoss Dark Archon", "Anywhere", cp);

            f.SkillWait(cp, 80);
            f.loop[cp] += 1;
         }
         else if (f.loop[cp] == 1)
         {
            f.SquareShape(cp, 1, "Target", 50, 50);
            f.SquareShape(cp, 1, "60 + 1n High Templar", 50, 50);
            KillUnitAt(All, "Target", "Anywhere", cp);
            KillUnitAt(All, "60 + 1n High Templar", "Anywhere", cp);

            f.SkillWait(cp, 80);

            f.loop[cp] += 1;
         }
         else if (f.loop[cp] == 2)
         {
            f.SquareShape(cp, 1, "Target", 50, 0);
            f.SquareShape(cp, 1, "Target", 100, 0);
            f.SquareShape(cp, 1, "60 + 1n High Templar", 50, 0);
            f.SquareShape(cp, 1, "60 + 1n High Templar", 100, 0);
            KillUnitAt(All, "Target", "Anywhere", cp);
            KillUnitAt(All, "60 + 1n High Templar", "Anywhere", cp);

            f.SkillWait(cp, 80);

            f.loop[cp] += 1;
         }
         else if (f.loop[cp] == 3)
         {         
            f.EdgeShape(cp, 1, "Kakaru (Twilight)", 0, 5, 100);
            f.EdgeShape(cp, 1, "60 + 1n Archon", 0, 5, 100);
            KillUnitAt(All, "Kakaru (Twilight)", "Anywhere", cp);
            KillUnitAt(All, "60 + 1n Archon", "Anywhere", cp);

            f.SkillWait(cp, 80);
            f.loop[cp] += 1;
         }
         else if (f.loop[cp] == 4)
         {         
            f.SquareShape(cp, 1, "40 + 1n Guardian", 50, 100);
            f.SquareShape(cp, 1, "40 + 1n Guardian", 100, 50);
            KillUnitAt(All, "40 + 1n Guardian", "Anywhere", cp);

            f.SkillWait(cp, 80);
            f.loop[cp] += 1;
         }
         else if (f.loop[cp] == 5)
         {         
            f.SquareShape(cp, 1, "40 + 1n Guardian", 100, 150);
            f.SquareShape(cp, 1, "40 + 1n Guardian", 150, 100);
            KillUnitAt(All, "40 + 1n Guardian", "Anywhere", cp);

            f.SkillWait(cp, 80);
            f.loop[cp] += 1;
         }
         else if (f.loop[cp] == 6)
         {         
            f.SquareShape(cp, 1, "Kakaru (Twilight)", 100, 150);
            f.SquareShape(cp, 1, "Kakaru (Twilight)", 150, 100);
            f.SquareShape(cp, 1, "Kakaru (Twilight)", 50, 100);
            f.SquareShape(cp, 1, "Kakaru (Twilight)", 100, 50);
            f.SquareShape(cp, 1, " Unit. Hoffnung 25000", 100, 150);
            f.SquareShape(cp, 1, " Unit. Hoffnung 25000", 150, 100);
            f.SquareShape(cp, 1, " Unit. Hoffnung 25000", 50, 100);
            f.SquareShape(cp, 1, " Unit. Hoffnung 25000", 100, 50);
            KillUnitAt(All, "Kakaru (Twilight)", "Anywhere", cp);
            KillUnitAt(All, " Unit. Hoffnung 25000", "Anywhere", cp);

            f.SkillWait(cp, 80);
            f.loop[cp] += 1;
         }
         else if (f.loop[cp] == 7)
         {         
            f.EdgeShape(cp, 1, "40 + 1n Mojo", 0, 5, 100);
            f.EdgeShape(cp, 1, "60 + 1n Archon", 0, 5, 100);
            KillUnitAt(All, "40 + 1n Mojo", "Anywhere", cp);
            KillUnitAt(All, "60 + 1n Archon", "Anywhere", cp);

            f.SkillWait(cp, 80);
            f.loop[cp] += 1;
         }
         else if (f.loop[cp] == 8)
         {         
            f.EdgeShape(cp, 1, "60 + 1n High Templar", 0, 5, 100);
            KillUnitAt(All, "60 + 1n High Templar", "Anywhere", cp);

            f.DotShape(cp, 1, "40 + 1n Marine", 100, 150);
            f.DotShape(cp, 1, "40 + 1n Marine", 150, 100);
            f.DotShape(cp, 1, "40 + 1n Marine", 50, 100);
            f.DotShape(cp, 1, "40 + 1n Marine", 100, 50);
            f.DotShape(cp, 1, "40 + 1n Mojo", 100, 150);
            f.DotShape(cp, 1, "40 + 1n Mojo", 150, 100);
            f.DotShape(cp, 1, "40 + 1n Mojo", 50, 100);
            f.DotShape(cp, 1, "40 + 1n Mojo", 100, 50);
            KillUnitAt(All, "40 + 1n Mojo", "Anywhere", cp);

            MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
            MoveUnit(All, "40 + 1n Marine", cp, "[Skill]Unit_Wait_ALL", f.location[cp]);
            Order("40 + 1n Marine", cp, "Anywhere", Attack, f.location[cp]);

            f.SkillWait(cp, 160);
            f.loop[cp] += 1;
         }
         else if (f.loop[cp] == 9)
         {         
            f.EdgeShape(cp, 1, "60 + 1n High Templar", 0, 5, 100);
            KillUnitAt(All, "60 + 1n High Templar", "Anywhere", cp);

            f.DotShape(cp, 1, "40 + 1n Marine", -100, -150);
            f.DotShape(cp, 1, "40 + 1n Marine", -150, -100);
            f.DotShape(cp, 1, "40 + 1n Marine", -50, -100);
            f.DotShape(cp, 1, "40 + 1n Marine", -100, -50);
            f.DotShape(cp, 1, "40 + 1n Mojo", -100, -150);
            f.DotShape(cp, 1, "40 + 1n Mojo", -150, -100);
            f.DotShape(cp, 1, "40 + 1n Mojo", -50, -100);
            f.DotShape(cp, 1, "40 + 1n Mojo", -100, -50);
            KillUnitAt(All, "40 + 1n Mojo", "Anywhere", cp);

            MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
            MoveUnit(All, "40 + 1n Marine", cp, "[Skill]Unit_Wait_ALL", f.location[cp]);
            Order("40 + 1n Marine", cp, "Anywhere", Attack, f.location[cp]);

            f.SkillWait(cp, 160);
            f.loop[cp] += 1;
         }
         else if (f.loop[cp] == 10)
         {         
            f.EdgeShape(cp, 1, "60 + 1n High Templar", 0, 5, 100);
            KillUnitAt(All, "60 + 1n High Templar", "Anywhere", cp);

            f.DotShape(cp, 1, "40 + 1n Marine", 100, -150);
            f.DotShape(cp, 1, "40 + 1n Marine", 150, -100);
            f.DotShape(cp, 1, "40 + 1n Marine", 50, -100);
            f.DotShape(cp, 1, "40 + 1n Marine", 100, -50);
            f.DotShape(cp, 1, "40 + 1n Mojo", 100, -150);
            f.DotShape(cp, 1, "40 + 1n Mojo", 150, -100);
            f.DotShape(cp, 1, "40 + 1n Mojo", 50, -100);
            f.DotShape(cp, 1, "40 + 1n Mojo", 100, -50);
            KillUnitAt(All, "40 + 1n Mojo", "Anywhere", cp);

            MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
            MoveUnit(All, "40 + 1n Marine", cp, "[Skill]Unit_Wait_ALL", f.location[cp]);
            Order("40 + 1n Marine", cp, "Anywhere", Attack, f.location[cp]);

            f.SkillWait(cp, 160);
            f.loop[cp] += 1;
         }
         else if (f.loop[cp] == 11)
         {         
            f.EdgeShape(cp, 1, "60 + 1n High Templar", 0, 5, 100);
            KillUnitAt(All, "60 + 1n High Templar", "Anywhere", cp);

            f.DotShape(cp, 1, "40 + 1n Marine", -100, 150);
            f.DotShape(cp, 1, "40 + 1n Marine", -150, 100);
            f.DotShape(cp, 1, "40 + 1n Marine", -50, 100);
            f.DotShape(cp, 1, "40 + 1n Marine", -100, 50);
            f.DotShape(cp, 1, "40 + 1n Mojo", -100, 150);
            f.DotShape(cp, 1, "40 + 1n Mojo", -150, 100);
            f.DotShape(cp, 1, "40 + 1n Mojo", -50, 100);
            f.DotShape(cp, 1, "40 + 1n Mojo", -100, 50);
            KillUnitAt(All, "40 + 1n Mojo", "Anywhere", cp);

            MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
            MoveUnit(All, "40 + 1n Marine", cp, "[Skill]Unit_Wait_ALL", f.location[cp]);
            Order("40 + 1n Marine", cp, "Anywhere", Attack, f.location[cp]);

            f.SkillWait(cp, 160);
            f.loop[cp] += 1;
         }
         else if (f.loop[cp] == 12)
         {         
            f.SkillWait(cp, 560);

            f.count[cp] += 1;
            f.loop[cp] = 0;
         }
      }
      else if (f.count[cp] == 3)
      {
         KillUnitAt(All, "40 + 1n Goliath", "Anywhere", cp);
         KillUnitAt(All, "40 + 1n Marine", "Anywhere", cp);

         f.SkillEnd(cp);
      }
   }
   if (f.delayB[cp] == 0)
   {
      if (f.count[cp] < 3)
      {
         if (f.loopB[cp] == 0)
         {
            f.SquareShape(cp, 1, "Protoss Dark Archon", 75, 75);

            KillUnitAt(All, "Protoss Dark Archon", "Anywhere", cp);

            f.SkillWaitB(cp, 160);

            f.loopB[cp] += 1;
         }
         else if (f.loopB[cp] == 1)
         {
            f.SquareShape(cp, 1, "60 + 1n Archon", 150, 0);

            KillUnitAt(All, "60 + 1n Archon", "Anywhere", cp);

            f.SkillWaitB(cp, 160);

            f.loopB[cp] = 0;
         }

      }
   }

}